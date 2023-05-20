# flask
from flask import Flask
from flask_cors import CORS
from flask import request

from langchain.agents import Tool
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory

from langchain.llms import OpenAI

from langchain.agents import initialize_agent
from langchain.tools import DuckDuckGoSearchRun
from langchain.tools import DuckDuckGoSearchRun
from langchain.utilities.wolfram_alpha import WolframAlphaAPIWrapper

from deep_translator import GoogleTranslator


import time
from datetime import datetime

open_ai_api_key = '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'

import os

os.environ["WOLFRAM_ALPHA_APPID"] = "T797XU-LURTPL7TA5"
os.environ["SERPAPI_API_KEY"] = "889a6a9700cf334a4e77d095be5eb0080d19d637e21a92544c1f02289b55a849"
os.environ["OPENAI_API_KEY"] = open_ai_api_key


app = Flask(__name__)
CORS(app)


my_memory = []

def initialize_agent_chain(translated):

    llm = OpenAI(temperature=0)


    search = DuckDuckGoSearchRun()
    wolfram = WolframAlphaAPIWrapper()
    tools = [
        Tool(
            name="Search",
            func=search.run,
            description="useful for when you need to answer questions about current events"
        ),
        Tool(
            name="Math",
            func=wolfram.run,
            description="useful for when you need to answer questions about math"
        ),
    ]


    now = datetime.now().second

    if len(my_memory) > 0 :

        temp =  my_memory.pop()
        my_memory.append(temp)
        diff = now - temp[1]
        if diff % 60 > 15:
            my_memory.clear()

    t = (translated, now) 
    my_memory.append(t)

    question = ''
    for element in my_memory:
        question += ' ' + element[0]

   

    agent_chain = initialize_agent(tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

    result = agent_chain.run(question)

    return result

@app.route('/ask-me', methods=['POST'])
def process_input():
    input_string = request.json['input']

    translated = GoogleTranslator(source='auto', target='en').translate(input_string)


    result = initialize_agent_chain(translated)

    result = GoogleTranslator(source='auto', target='ar').translate(result)

    return result

if __name__ == '__main__':
    app.run(debug=True)
