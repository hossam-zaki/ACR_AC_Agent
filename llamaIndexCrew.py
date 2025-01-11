import os
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import LlamaIndexTool
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.openai import OpenAI
from llama_index.llms.groq import Groq
from llama_index.llms.ollama import Ollama



reader = SimpleDirectoryReader(input_dir='Narrative_PDFs')
docs = reader.load_data()

llm = LLM(
    model="groq/llama-3.1-70b-versatile",
    temperature=0.0
)

# llm = LLM(
#     model="ollama/llama3.2",
#     base_url="http://localhost:11434",
#     temperature=0.0
# )


llm_LI = Groq(model="llama-3.1-70b-versatile")
#llm_LI = Ollama(model="llama3.2", request_timeout=60.0)
index = VectorStoreIndex.from_documents(docs)
query_engine = index.as_query_engine(similarity_top_k=5, llm=llm_LI)

# try out query engine tool

query_tool = LlamaIndexTool.from_query_engine(
    query_engine,
    name="Appropriateness Criteria Tool",
    description="Use this tool to lookup the ACR Appropriateness criteria for the most appropriate imaging or procedure for a given clinical vignette.",
)

# Define your agents with roles and goals
image_or_proc_agent = Agent(
    role="Procedure or Imaging Determiner",
    goal="Determine if the prompt is asking for imaging or a procedure",
    backstory="""You excell at knowing what people are asking. You need to determine if the propmt is asking 
        for imaging or a procedure.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

AC_analyst = Agent(
    role="Imaging or Procedural Appropriateness Administrator",
    goal="Take in a clinical vignette, and tell me the most appropriate next step is",
    backstory="""You are an Imaging or Procedural Appropriateness Administrator with expertise in Interventional Radiology.
    Given clinical vignettes, you are able to tell me the most appropriate next step and why.
    If you tell me the imaging, please be as specific as possible, including utilization of contrast or location of the imaging. The PDFs you are searching have a clinical vignette, followed by a table telling you the level of
    appropriateness of the intervention/imaging. What you need to pay attention to are the ones that say Usually Appropriate. Once you have an answer, stop""",
    llm=llm,
    tools=[query_tool],
)

# Create tasks for your agents
image_or_proc = Task(
    description="""First step to determine if the prompt is asking for imaging or a procedure. Here's the prompt {user_question}""",
    expected_output="A sentence if the prompt is asking for an imaging or a procedure",
    agent=image_or_proc_agent,
)

ac_task = Task(
    description="Take this clinical vignette: {user_question}, and then determine what the most appropriate next step is.",
    expected_output="The task is complete when either a procedure or an imaging technology is mentioned to be the most appropriate, as well as a clear explanation for the inputted clinical vignette",
    agent=AC_analyst
)

# Instantiate your crew with a sequential process
crew = Crew(
    agents=[AC_analyst],
    tasks=[ac_task],
    verbose=True,
    process=Process.sequential
)

result = crew.kickoff(
    inputs={"user_question": """
Suspected thrombosis of the upper or lower extremity hemodialysis access, marked by absent
pulse and thrill on physical examination. Initial imaging to guide interventional radiologic
therapy options.
            """}
)