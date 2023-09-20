import warnings
import pandas as pd

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain


warnings.filterwarnings('ignore')

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file

llm_model = "gpt-3.5-turbo"

data_frame = pd.read_csv("C:/Users/Andrei_Ruzaev/PycharmProjects/pythonProject/Data.csv")

result = data_frame.head()

print(result)

llm = ChatOpenAI(temperature=0.9, model=llm_model)

prompt = ChatPromptTemplate.from_template(
    "What is the best name to describe a company that makes {product}?"
)

chain = LLMChain(llm=llm, prompt=prompt)

product = "Queen Size Sheet Set"
result = chain.run(product)

print(result)
