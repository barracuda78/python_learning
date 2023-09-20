import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
from langchain.agents.agent_toolkits import create_python_agent
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType
from langchain.tools.python.tool import PythonREPLTool
from langchain.python import PythonREPL
from langchain.chat_models import ChatOpenAI


import warnings
warnings.filterwarnings("ignore")

llm_model = "gpt-3.5-turbo"

llm = ChatOpenAI(temperature=0, model=llm_model)

tools = load_tools(["llm-math","wikipedia"], llm=llm)

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose=True)

result = agent("What is the 25% of 300?")

print("----------------math result:--------------------")
print(result)

##########################################################################

question = "Tom M. Mitchell is an American computer scientist \
and the Founders University Professor at Carnegie Mellon University (CMU)\
what book did he write?"
result = agent(question)
print("----------------wiki result:--------------------")
print(result)
