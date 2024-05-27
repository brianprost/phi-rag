import streamlit as st
from phi.tools.duckduckgo import DuckDuckGo
from phi.assistant import Assistant
from phi.llm.ollama import Ollama
import time

st.title("AI Search")
st.caption("Since Google can't do AI search")

system_prompt = f"Generate a comprehensive and informative answer (but no more than 80 words) for a given question solely based on the provided web Search Results (URL and Summary). You must only use information from the provided search results. Use an unbiased and journalistic tone. Use this current date and time: {time.strftime("%Y-%m-%d %H:%M:%S")}. Combine search results together into a coherent answer. Do not repeat text. Only cite the most relevant results that answer the question accurately. If different results refer to different entities with the same name, write separate answers for each entity."

assistant = Assistant(
    llm=Ollama(model="llama3:latest"),
    description=system_prompt,
    tools=[DuckDuckGo()],
)

query = st.text_input("Where knowledge begins", type="default")
if query:
    response = assistant.run(query, stream=True)
    st.write(response)
