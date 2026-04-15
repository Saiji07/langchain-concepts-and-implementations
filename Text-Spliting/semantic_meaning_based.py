from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-2-preview"
)
text_spliter=SemanticChunker(
    embeddings,breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)

sample="""Yesterday was one of the most exciting days of my life. I finally got selected for the internship I had been preparing for months. I felt proud, confident, and extremely happy. Everything seemed to be going perfectly.

However, later in the evening, things took a sudden turn. I received a message that my close friend had failed an important exam. I felt really sad and helpless. It reminded me that success and failure are often very close to each other.

Today, I woke up with mixed feelings. On one hand, I am still happy about my achievement, but on the other hand, I am worried about my friend. Life feels complicated sometimes, full of ups and downs.

In the afternoon, I decided to call my friend and motivate him. After talking for a while, he sounded better, and I felt relieved. Helping someone in need gave me a sense of satisfaction.

By the end of the day, I realized that emotions are never constant. Happiness, sadness, stress, and relief all come and go. What matters most is how we handle these situations and support the people around us."""

docs=text_spliter.create_documents([sample])
print(len(docs))
print(docs)
