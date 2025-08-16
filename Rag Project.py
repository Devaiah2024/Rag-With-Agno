print("Step 1: Import the libraries")


print("Topic: Creating RAG project with Agno")
print()
print("Step 1: Import the libraries ")
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.lancedb import LanceDb, SearchType

print("Step 2: Define Vector Database")

db_uri = "tmp/lancedb"

print("Step 3: Load Knowledge from a PDF")

obj = LanceDb(
            table_name = "recipes",
            uri = db_uri,
            search_type = SearchType.vector
            )


knowledge_base = PDFUrlKnowledgeBase(

                urls=["https://phi-
                public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
                vector_db= obj,
                )

print("Step 4: Embed and Store")

knowledge_base.load(upsert = True)

print("Step 5: Create the RAG Agent")

rag_agent = Agent(
            model = OpenAIChat(id = "gpt-4o"),
            agent_id = "rag-agent",
            knowledge = knowledge_base,
            )


print("Step 6: Ask Questions and Get Responses")

query = "How do I make Pad Thai?"
response = rag_agent.run(query)
print("Bot:", response.content)