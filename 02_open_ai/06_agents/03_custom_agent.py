import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
from langchain.agents.agent_toolkits import create_python_agent
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType
from langchain.tools.python.tool import PythonREPLTool
from langchain.python import PythonREPL
from langchain.chat_models import ChatOpenAI
from langchain.agents import tool
from datetime import date

import warnings
warnings.filterwarnings("ignore")

llm_model = "gpt-3.5-turbo"

llm = ChatOpenAI(temperature=0, model=llm_model)

@tool
def time(text: str) -> str:
    """Returns todays date, use this for any \
    questions related to knowing todays date. \
    The input should always be an empty string, \
    and this function will always return todays \
    date - any date mathmatics should occur \
    outside this function."""
    return str(date.today())

tools = load_tools(["llm-math","wikipedia"], llm=llm)

agent= initialize_agent(
    tools + [time],
    llm,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose=True)

#  The agent will sometimes come to the wrong conclusion (agents are a work in progress!).
#  If it does, please try running it again.


try:
    result = agent("whats the date today?")
except:
    print("exception on external access")
