import os

os.environ["GOOGLE_API_KEY"] = ""

#AI LLM MODEL ACCESS
from langchain_google_genai import ChatGoogleGenerativeAI

google_llm = ChatGoogleGenerativeAI( model="gemini-2.5-flash", temperature=0 )

response = google_llm.invoke(" How to list file systems on linux machine. ")

print(response.content)

