from functions import check_vecdb, get_response
from flask import Flask, render_template, request
app = Flask(__name__)

#Create Vector DB
persist_dir = "DB"
documentsfolder="documents"
db=check_vecdb(documentsfolder,persist_dir)

@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')
@app.route('/chatbot', methods=['POST'])
def financeaiwriter():

    ai_writer_template = """
    -Give a detailed Answer of the user's questions based on the below context. You are trained on the 
    consitution of Pakistan.
    -Include all the relevant clauses with statements.
    -make bullets and return a structured answer
    -the answer should follow the below given structure:
        *short explanation of the answer
        * relevant clauses with article numbers and statements. list all the relevant clauses and articles
        *additional information
        *conclusion
    -If the context doesn't contain any relevant information to the question, don't make something up and just 
    say "Your question does not match my knowledhe base. Please ask something related to consitution of Pakistan.":

    <context>
    {context}
    </context>
    \n\n

    Now write a short answer for the following question:
    Question: "{Question}"
    Answer:"""

    question=request.form['question']

    docs = db.similarity_search(question)
    new_context = ""
    for document in docs:
        new_context += document.page_content

    response = get_response(question, new_context, ai_writer_template)
    return response

if __name__ == "__main__":
    app.run(debug=True)