
#Note Typeddict is supported in open ai not in gemini 

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class Review(TypedDict):
    summary:Annotated[str,"a breif summary of the review"]
    sentiment:Annotated[str,"return sentiment of review in positive,negative or neutral"]

structured_model=model.with_structured_output(Review)


result=structured_model.invoke("""The display is clear and comfortable for reading code for long hours, and the battery backup is decent, so you can work without charging frequently. Overall, this phone is suitable for learning programming, practicing problems, and doing light development work. However, for heavy tasks like large app development or machine learning, a laptop would still be a better option.""")
print(result)
