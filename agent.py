import nest_asyncio
nest_asyncio.apply()
import torchvision
torchvision.disable_beta_transforms_warning()
import os
import json
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.core.tools import FunctionTool
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import FunctionCallingAgent, AgentRunner, FunctionCallingAgentWorker
from llama_parse import LlamaParse
from llama_index.core.objects import ObjectIndex
from base_1 import GradioAgentChatPack



class ACRAgent():
    def __init__(self,
                 llama_parse_api_key=None,
                 file_descriptions_path='file_descriptions.json',
                 llm="llama3.3",
                 embed_model="BAAI/bge-base-en-v1.5"):
        
        # ollama
        self.llm = Ollama(model=llm, request_timeout=360.0, temperature=0)

        # bge-base embedding model
        Settings.embed_model = HuggingFaceEmbedding(model_name=embed_model)
        Settings.llm = self.llm
        
        format_title = lambda x: x.lower()

        if llama_parse_api_key is not None:
            parser = LlamaParse(
                result_type="markdown",
                premium_mode=False,  # "markdown" and "text" are available
                api_key = llama_parse_api_key
            )
        file_extractor = {".pdf": parser} if llama_parse_api_key is not None else None

        with open(file_descriptions_path, 'r') as file:
            file_descriptions = json.load(file)

        pdf_dir = 'data'

        query_engine_tools = []
        agents = {}

        # Iterate through each PDF in the directory
        for file_name in os.listdir(pdf_dir):
            if file_name.endswith(".pdf"):
                # Load the document
                file_path = os.path.join(pdf_dir, file_name)
                reader = SimpleDirectoryReader(input_files=[file_path], file_extractor=file_extractor)
                #reader = SimpleDirectoryReader(input_files=[file_path])
                documents = reader.load_data()
                description = file_descriptions[format_title(file_name[:-4])]
                
                # Create an index for the document
                vector_index = VectorStoreIndex.from_documents(documents)
                query_engine_tool = QueryEngineTool.from_defaults(
                    vector_index.as_query_engine(
                        similarity_top_k=3,
                    ),
                    name=f"{file_name[:-4]} query engine",
                    description=description
                )
                
                query_engine_tools.append(query_engine_tool)

                agents[f"{format_title(file_name[:-4])}"] = FunctionCallingAgent.from_tools(
                    [query_engine_tool],
                    llm = self.llm,
                    verbose=False,
                    system_prompt=f"""\
                    You are a specialized agent designed to answer questions about {format_title(file_name[:-4])} using the American \
                    College of Radiology (ACR) appropriateness criteria. You have access to a tool that allows you to query a document \
                    from the ACR regarding {format_title(file_name[:-4])}. This document {description.lower()} \
                    When using the query tool, explicitly ask "provide any relevant tables and information" in addition to your usual query. \
                    In your response, provide as much relevant detail from the documents as possible. \
                    If the tool provides a table with next steps, format the table in your response as a json. Do not \
                    come up with ratings that are not explicitly given in the tools. \
                    If multiple tables are returned, or if additional information is needed to narrow recommendations, summarize the information \
                    required to best inform which recommendations to make. \
                    You must always use at least one of the tools provided when answering a question. Do NOT rely on prior knowledge.
                    """
                )

        tools = []
        for agent_name, agent in agents.items():
            tool = QueryEngineTool(
                query_engine = agent,
                metadata=ToolMetadata(
                    name=f'tool_{agent_name}',
                    description=f'This tool uses the {agent_name} agent to answer queries. {agent_name} has access to a document which {file_descriptions[agent_name].lower()}'
                )
            )
            tools.append(tool)

        fallback_tool = FunctionTool.from_defaults(
            lambda: 'No relevant information contained in the American College of Radiology (ACR) appropriateness criteria',
            name="Fallback Tool",
            description="Handles queries with no relevance to interventional radiology  American College of Radiology (ACR) appropriateness criteria.\
            This tool can be called when no other tool can."
        )
        tools.append(fallback_tool)

        obj_index = ObjectIndex.from_objects(
            tools + [fallback_tool],
            index_cls=VectorStoreIndex,
        )

        obj_retriever = obj_index.as_retriever(similarity_top_k=3)

        agent_worker = FunctionCallingAgentWorker.from_tools(
            tool_retriever=obj_retriever,
            llm=Settings.llm, 
            system_prompt=""" \
            You are a top-level agent designed to answer queries regarding planning, follow-up, and next steps for various interventional radiology \
            scenarios. Choose the most appropriate agent in the object index based on the user query. These agents have access to documents from \
            the American College of Radiology (ACR) appropriateness criteria. The agent will output a json if there is a matching scenario in its document. \
            You will receive queries regarding planning, follow-up, and next steps for various scenarios in interventional radiology and medicine more \
            generally. Use the agents and tools provided to you to best respond to these queries as if you were answering a question for a physician and \
            in a way that would be most useful for clincial practice. \
            For example, if a next step is regarded as "usually appropriate," you should respond as such. If you receive a json format text, interpret the text \
            and use the information in your response. Do not respond with json text. \
            If a response cannot be answered with the ACR Appropriateness criteria or the agents available to you, \
            state that the information is not contained within the ACR AC. \
            Prompt the user for additional information if it would be useful in narrowing down the next steps or recommendations. \
            Always use a provided agent to answer the question. Do NOT rely on prior knowledge.\
            """,
            verbose=False
        )

        self.top_agent = AgentRunner(agent_worker)

    def chat(self, input):
        return str(self.top_agent.chat(input))

    def query(self, input):
        return str(self.top_agent.query(input))

if __name__ == '__main__':
    agent = ACRAgent(llama_parse_api_key='llx-YHDQbGSWpgHYl1nlnNBp588THUnaE4ryaTgc4mUqaZEF9R5u')
    grAg = GradioAgentChatPack(agent=agent)
    grAg.run()
    # agent = ACRAgent()
    # print('Ask this agent about the appropriateness of IR planning and follow up.')
    # while True:
    #     print(agent.chat(input('Input: ')))