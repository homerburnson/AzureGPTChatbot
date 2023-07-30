from flask import Flask, request, jsonify, render_template
from langchain import OpenAI
from llama_index import SimpleDirectoryReader, VectorStoreIndex, LLMPredictor, ServiceContext, StorageContext, load_index_from_storage
import os
import sys

os.environ["OPENAI_API_KEY"] = "INSERT KEY HERE"

def construct_index(directory_path):
    num_outputs = 512
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.7, model_name="gpt-3.5-turbo", max_tokens=num_outputs))
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
    docs = SimpleDirectoryReader(directory_path).load_data()
    index = VectorStoreIndex.from_documents(docs, service_context=service_context)
    index.storage_context.persist(persist_dir="training/index")
    return index

def chatbotanswer(input_text):
    storage_context = StorageContext.from_defaults(persist_dir="training/index")
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()
    response = query_engine.query(input_text)
    print(response)
    return response.response

app = Flask(__name__)

@app.route("/", methods=["GET"])
@app.route("/chatbot", methods=["GET", "POST"])
def chatbot():
    if request.method == "POST":
        data = request.json
        user_message = data["message"]
        parsedresponse = chatbotanswer(user_message)
        response = {"response": parsedresponse}
        return jsonify(response)
    else:
        return render_template("/index.html")

if __name__ == "__main__" and len(sys.argv) > 1:
    construct_index("docs")
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)