import streamlit as st
import openai

# exercise 11
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# exercise 12
from langchain.memory import ConversationBufferWindowMemory

# exercise 13
from langchain.document_loaders import TextLoader, PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import LanceDB
import lancedb
import os
import tempfile

# exercise 15
import sqlite3
import pandas as pd
from datetime import datetime

# exercise 16
from langchain.agents import ConversationalChatAgent, AgentExecutor
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory
from langchain.tools import DuckDuckGoSearchRun

# Exercise 17
from langchain.agents import tool
import json

# Exercise 18
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI
import matplotlib.pyplot as plt

from part1 import ex1, ch1, ex2, ex3, ex4a, ex4b, ch4, ex5, ex6, ch6, ex8, ch8, ex9_basebot, ex10_basebot, ch10_basebot, chat_completion_stream_prompt
from part2 import ex11a, ex11b, ch11, ex12, ch12, ex13, ex14_basebot, prompt_inputs_form
from part3 import ex15, ch15, ex16_agent_bot, ex17_agent_bot
from part4 import ex18_pandas_AI

# Global ex 13
cwd = os.getcwd()
WORKING_DIRECTORY = os.path.join(cwd, "database")

if not os.path.exists(WORKING_DIRECTORY):
	os.makedirs(WORKING_DIRECTORY)
# ex15
DB_NAME = os.path.join(WORKING_DIRECTORY, "default_db")

st.title("GenAI codecraft workshop")

def main():
	# initialize session state, from ch4
	if "name" not in st.session_state:
		st.session_state.name = "Yoda"

	if "age" not in st.session_state:
		st.session_state.age = 999

	if "gender" not in st.session_state:
		st.session_state.gender = "male"

	if "prompt_template" not in st.session_state:
		st.session_state.prompt_template = "Speak like Yoda from Star Wars for every question that was asked, do not give a direct answer but ask more questions in the style of wise Yoda from Star Wars"

	#st.write("Hello world!")
	# ex1()
	# ch1()
	# ex2()
	# ex3()
	# ex4a()
	# ex4b()
	# ch4()
	# ex5()
	# ex6()
	# ch6()
	# ex8()
	# ch8()
	# ex9_basebot()
	# ex10_basebot()
	# ch10_basebot()
	# ex11a()
	# ex11b()
	# ch11()
	# ex12()
	# ch12()
	# ex13()
	# ex14_basebot()
	# ex15()
	# ch15()
	# ex16_agent_bot()
	# ex17_agent_bot()
	ex18_pandas_AI()

if __name__ == "__main__":
	main()