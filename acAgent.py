# import nest_asyncio
# nest_asyncio.apply()

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.core.tools import FunctionTool
from llama_index.core.tools import QueryEngineTool
from llama_index.core.agent import ReActAgent, FunctionCallingAgent, AgentRunner, FunctionCallingAgentWorker
import os
from base_1 import GradioAgentChatPack

import torchvision
torchvision.disable_beta_transforms_warning()

# bge-base embedding model
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# ollama
Settings.llm = Ollama(model="llama3.1", request_timeout=360.0, temperature=0)

pdf_dir = 'data'

query_engine_tools = []

# Iterate through each PDF in the directory
for file_name in os.listdir(pdf_dir):
    if file_name.endswith(".pdf"):
        # Load the document
        file_path = os.path.join(pdf_dir, file_name)
        reader = SimpleDirectoryReader(input_files=[file_path])
        documents = reader.load_data()
        
        # Create an index for the document
        vector_index = VectorStoreIndex.from_documents(documents)
        query_engine_tool = QueryEngineTool.from_defaults(
            vector_index.as_query_engine(
                similarity_top_k=3,
            ),
            name=f"{file_name} query engine",
            description=f"Query engine for the American College of Radiology (ACR) appropriateness criteria on {file_name[:-4]}."
        )
        
        query_engine_tools.append(query_engine_tool)

fallback_tool = FunctionTool.from_defaults(
    lambda x: 'No relevant information contained in the American College of Radiology (ACR) appropriateness criteria',
    name="Fallback Tool",
    description="Handles queries no other tool can."
)

agent = FunctionCallingAgent.from_tools(
    query_engine_tools + [fallback_tool],
    llm=Settings.llm,
    system_prompt='You are a specialized agent designed to answer queries about the planning and follow up \
    for topics related to interventional radiology based on the American College of Radiology (ACR) appropriateness criteria. \
    Answer using only information from one or more of the provided tools. \
    Do not answer from prior knowledge under any circumstances. \
    If no appropriate tool exists or if the tools do not provide sufficient context, do not answer the query. Instead, \
    indicate that the necessary information is not available in the ACR appropriateness criteria.',
    verbose=True
)

agent = FunctionCallingAgent.from_tools(
    query_engine_tools + [fallback_tool],
    llm=Settings.llm,
    system_prompt='You are a specialized agent designed to answer queries about the planning and follow up \
    for topics related to interventional radiology based on the American College of Radiology (ACR) appropriateness criteria.\
    Given clinical vignettes, you are able to tell me the most appropriate next step and why. \
    If you tell me the imaging, please be as specific as possible, including utilization of contrast or location of the imaging.\
    The PDFs you are searching have a clinical vignette, followed by a table telling you the level of \
    appropriateness of the intervention/imaging. What you need to pay attention to are the ones that say Usually Appropriate. \
    If you tell me multiple potential options or next steps, tell me which are more appropriate. If one or more options is "Usually Appropriate",\
    explicitly state so. Answer using only information from one or more of the provided tools.\
    Do not answer from prior knowledge under any circumstances. If no appropriate tool exists or if the tools do not provide sufficient\
    context, do not answer the query. Instead, indicate that the necessary information is not available in the ACR\
    appropriateness criteria. Cite your sources. Once you have an answer, stop',
    verbose=True
)


grAg = GradioAgentChatPack(agent=agent)

grAg.run()
# response = agent.chat(
#     'What kind of catheter should I use for central line? '
#     'On a separate note, I also want to know if my patient with a DVT needs a stent. '
#     'Also, do you know why blood is red? '
# )

# response = agent.chat(
#     '30 year old woman with fibroids who still desires pregnancy but is having trouble with fertility. What is the best next treatment plan?'
# )


# response = agent.chat(
#     'Postmenopausal patient with uterine fibroids, symptomatic with heavy uterine bleeding or \
#     bulk symptoms (eg, pressure, pain, fullness, bladder, or bowel symptoms). Negative \
#     endometrial biopsy. Next step.'
# )
