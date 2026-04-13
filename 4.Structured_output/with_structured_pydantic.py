
#Note Typeddict is supported in open ai not in gemini 

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional,Literal
from pydantic import BaseModel, Field

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class Review(BaseModel):
    key_themes:list[str]= Field(description="write down all the key themes discussed in the review")
    summary:str=Field(description="breif summary of review")
    sentiment: Literal["positive","negative","neutral"] = Field(description="return sentiment of review positive, negative or nueutral")
    pros:Optional[list[str]] =Field(description="write down all the pros of product on which review is based on")
    cons:Optional[list[str]] =Field(description="write down all the cons of product on which review is based on")
    name:Optional[str] =Field(description="name of the person who given the review ")
    

structured_model=model.with_structured_output(Review)


result=structured_model.invoke("""The phone performs adequately for everyday tasks and basic coding activities.The display is decent and readable for long sessions, but it is not exceptional. Battery life is average and usually lasts a full day with moderate usage. While it can handle light development work and practice problems, it may struggle with more demanding tasks. Overall, the device offers a balanced experience with both strengths and limitations, making it neither particularly impressive nor disappointing.""")
print(result)
