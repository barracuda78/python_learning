import warnings
from langchain import LLMChain

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import SimpleSequentialChain


warnings.filterwarnings('ignore')

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file

llm = ChatOpenAI(temperature=0.9, model="gpt-3.5-turbo")

first_prompt = ChatPromptTemplate.from_template(
    "What is the best name to describe a company that makes {product}?"
)

chain_one = LLMChain(llm=llm, prompt=first_prompt)

second_prompt = ChatPromptTemplate.from_template(
    "Write a 20 words description for the following \
    company:{company_name}"
)
chain_two = LLMChain(llm=llm, prompt=second_prompt)

third_prompt = ChatPromptTemplate.from_template("What is the first word of the following description:{description}")
chain_three = LLMChain(llm=llm, prompt=third_prompt)

overall_simple_chain = SimpleSequentialChain(chains=[chain_one, chain_two, chain_three], verbose=True)
product = "Queen Size Sheet Set"
result = overall_simple_chain.run(product)

print(result)
