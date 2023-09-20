from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationTokenBufferMemory


llm_model = "gpt-3.5-turbo"
llm = ChatOpenAI(temperature=0.0, model=llm_model)
memory = ConversationTokenBufferMemory(llm=llm, max_token_limit=50)  # you may change max_token_limit


memory.save_context({"input": "AI is what?!"},
                    {"output": "Amazing!"})
memory.save_context({"input": "Backpropagation is what?"},
                    {"output": "Beautiful!"})
memory.save_context({"input": "Chatbots are what?"},
                    {"output": "Charming!"})

memory.load_memory_variables({})

print(memory.buffer)
