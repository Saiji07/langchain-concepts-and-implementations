# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()

# model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
# chat_history=[]

# while True:
#     print("enter exit to end conversation")
#     user_input=input('You : ')
#     chat_history.append(user_input)
#     if user_input == 'exit':
#         break
#     result=model.invoke(chat_history)
#     chat_history.append(result)
#     print("AI : ",result.content)


# print("Thank You for visit")

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")
chat_history=[
    SystemMessage(content='you are a helpful assistant')
]

while True:
    print("enter exit to end conversation")
    user_input=input('You : ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI : ",result.content)

print(chat_history)
print("Thank You for visit")

