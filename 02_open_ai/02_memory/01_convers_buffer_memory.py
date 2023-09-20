from langchain import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory


llm_model = "gpt-3.5-turbo"
llm = ChatOpenAI(temperature=0.0, model=llm_model)
memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)
conversation.predict(input="Hi, my name is Andrew")
conversation.predict(input="What is 1+1?")
conversation.predict(input="What is my name?")

print(memory.buffer)

memory.load_memory_variables({})

memory = ConversationBufferMemory()

memory.save_context({"input": "Hi"},
                    {"output": "What's up"})

print(memory.buffer)

memory.load_memory_variables({})

memory.save_context({"input": "Not much, just hanging"},
                    {"output": "Cool"})

print(memory.buffer)

memory.load_memory_variables({})

