from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import CSVLoader
from langchain.vectorstores import DocArrayInMemorySearch
from IPython.display import display, Markdown
from langchain.indexes import VectorstoreIndexCreator

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())  # read local .env file

llm_model = "gpt-3.5-turbo"

file = 'C:/Users/Andrei_Ruzaev/PycharmProjects/pythonProject/shirts.txt'
loader = CSVLoader(file_path=file)


index = VectorstoreIndexCreator(vectorstore_cls=DocArrayInMemorySearch).from_loaders([loader])

query = "Please list all shirts with sun protection."

response = index.query(query)

# result = display(Markdown(response))
print(response)
