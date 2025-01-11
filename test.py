from crewai import Agent, Task, Crew, Process, LLM
from crewai.knowledge.source.base_knowledge_source import BaseKnowledgeSource
import requests
from datetime import datetime
from typing import Dict, Any
from pydantic import BaseModel, Field
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, PromptTemplate
from llama_index.llms.anthropic import Anthropic
from llama_parse import LlamaParse

from crewai_tools import DirectorySearchTool


# For dynamic directory specification at runtime
tool = DirectorySearchTool()

# For fixed directory searches
tool = DirectorySearchTool(directory='Narrative_PDFs')
llm = LLM(
    model="groq/llama-3.1-70b-versatile",
    temperature=0.0
)


# Create specialized agent
AC_analyst = Agent(
    role="Imaging or Procedural Appropriateness Administrator",
    goal="Take in a clinical vignette, and tell me the most appropriate next step is, whether it be imaging, treatment, or conservative management. ",
    backstory="""You are an Imaging or Procedural Appropriateness Administrator with expertise in Interventional Radiology.
    Given clinical vignettes, you are able to tell me the most appropriate next step and why. First, decide if they want imaging or a procedure.
    If you tell me the imaging, please be as specific as possible, including utilization of contrast or location of the imaging. The PDFs you are searching have a clinical vignette, followed by a table telling you the level of
    appropriateness of the intervention/imaging. What you need to pay attention to are the ones that say Usually Appropriate""",
    llm=llm,
    tools=[tool]
)

# Create task that handles user questions
analysis_task = Task(
    description="Take this clinical vignette: {user_question}",
    expected_output="Most next step and why",
    agent=AC_analyst
)

# Create and run the crew
crew = Crew(
    agents=[AC_analyst],
    tasks=[analysis_task],
    verbose=True,
    process=Process.sequential
)

# Example usage
result = crew.kickoff(
    inputs={"user_question": """
Reproductive age patient with uterine fibroids desiring pregnancy and experiencing
reproductive dysfunction. Initial therapy
            """}
)
