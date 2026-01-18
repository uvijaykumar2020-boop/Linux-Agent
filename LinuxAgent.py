import os

os.environ["GOOGLE_API_KEY"] = ""

#AI LLM MODEL ACCESS
from langchain_google_genai import ChatGoogleGenerativeAI

google_llm = ChatGoogleGenerativeAI( model="gemini-1.5-preview", temperature=0.70 )

response = google_llm.invoke(" Tell me how to check the system memory usage on a Linux machine. ")

print(response.content)

