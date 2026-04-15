from langchain.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.schema import Document
from dotenv import load_dotenv
load_dotenv()
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-2-preview"
)

docs = [
     Document(
    page_content="""MS Dhoni is one of the most successful captains in cricket history. 
He led India to multiple ICC trophies, including the T20 World Cup 2007, ODI World Cup 2011, 
and Champions Trophy 2013. Known for his calm demeanor and finishing abilities, 
Dhoni is widely regarded as one of the greatest wicketkeeper-batsmen of all time.""",
    
    metadata={
        "ipl_team": "Chennai Super Kings"
    }
),

    Document(
        page_content="""Virat Kohli is one of the greatest modern-day batsmen. 
He is known for his aggressive batting style, consistency, and leadership. 
Kohli has scored numerous centuries across all formats and played a key role in India's success.""",
        metadata={
            "ipl_team": "Royal Challengers Bangalore"
        }
    ),

    Document(
        page_content="""Rohit Sharma is an elegant batsman and the captain of the Indian cricket team. 
He is famous for his ability to score big hundreds, including multiple double centuries in ODIs. 
Rohit is also a successful IPL captain.""",
        metadata={
            "ipl_team": "Mumbai Indians"
        }
    ),

    Document(
        page_content="""Jasprit Bumrah is one of the best fast bowlers in the world. 
He is known for his unique bowling action, deadly yorkers, and performance in death overs. 
Bumrah has been crucial in all formats for India.""",
        metadata={
            "ipl_team": "Mumbai Indians"
        }
    ),

    Document(
        page_content="""Matheesha Pathirana is a Sri Lankan fast bowler known for his slingy action similar to Lasith Malinga. 
He is a specialist in death overs and plays for Chennai Super Kings in the IPL.""",
        metadata={
            "ipl_team": "Chennai Super Kings"
        }
    ),

    Document(
        page_content="""Ravindra Jadeja is one of the best all-rounders in the world. 
He is known for his sharp fielding, accurate left-arm spin bowling, and useful batting in the middle order. 
Jadeja has been a key player for India and Chennai Super Kings.""",
        metadata={
            "ipl_team": "Chennai Super Kings"
        }
    )

]


vector_store=Chroma(
    embedding_function=embeddings,
    persist_directory='chroma_db',
    collection_name='example'
)
vector_store.add_documents(docs)
result=vector_store.get(include=['embeddings','documents','metadatas'])

result1=vector_store.similarity_search(
    query='who among these are bowler?',
    k=2
)
print(result1)
result2=vector_store.similarity_search_with_score(
    query='who among these are bowler?',
    k=3
)
print(result2)

# print(result)

