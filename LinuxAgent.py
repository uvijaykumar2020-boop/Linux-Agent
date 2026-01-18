import os

os.environ["GOOGLE_API_KEY"] = ""

#AI LLM MODEL ACCESS
from langchain_google_genai import ChatGoogleGenerativeAI

google_llm = ChatGoogleGenerativeAI( model="gemini-2.5-flash", temperature=0 )

#response = google_llm.invoke(" How to list file systems on linux machine. ")

#print(response.content)

from langchain.agents import create_agent
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

tools = [shell_tool]

# Agent creation with model and tools passing.
agent = create_agent(
        model=google_llm,   
        tools=tools
)

UserPrompt = input (" Please enter your requirement")

system_message = SystemMessage(
                """
                You are the Linux Administrator and give me last results
                """
)
                
input_message = HumanMessage(content=UserPrompt)

messages = [
     system_message,
	 input_message
]

# Invoke (replacement for .run
result = agent.invoke({
"messages":messages
})

print(result)