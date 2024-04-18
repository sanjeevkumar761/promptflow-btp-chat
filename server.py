import os
from flask import Flask, request
from promptflow.client import load_flow
from promptflow.entities import AzureOpenAIConnection
from promptflow.entities import FlowContext
import subprocess

app = Flask(__name__)
port = int(os.environ.get('PORT', 3000))

llm_connection = AzureOpenAIConnection(
    name="llm_connection", api_key=os.getenv("AZURE_OPENAI_API_KEY"), api_base=os.getenv("AZURE_OPENAI_API_BASE")
)

f = load_flow(".")
chat_history=[]
f.context = FlowContext(
    # override flow connections with connection object created above
    connections={"chat": {"connection": llm_connection}}
)


@app.route('/chat')
def chat():
    question=request.args.get("question")
    result = f(question=question, chat_history=chat_history)
    chat_history.append({"inputs": {'question': question}, "outputs": {'answer': result}})
    return result["answer"]
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)