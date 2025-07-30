from langchain.agents import initialize_agent, AgentType
from langchain.prompts import PromptTemplate
from geminillm import GeminiLLM
from agent_config import tools

llm = GeminiLLM(api_key="your-gemini-api-key")

with open("prompt_template.txt", "r") as f:
    template = f.read()

prompt = PromptTemplate(
    input_variables=["input"],
    template=template
)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    agent_kwargs={"prefix": template}
)

def run_agent(query):
    return agent.run(query)
