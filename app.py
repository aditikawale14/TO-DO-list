from flask import Flask,render_template

app = Flask(__name__)

todos = [
    {"sno":1,"tilte":"Sample task",
     "desc":"This is a sample task for todo list", "date_created": "08-08-26", "status":"Pending"}
]

@app.route("/")
def home():
    return render_template("index.html",allTodos = todos)

if __name__ == "__main__":
    app.run(debug=True)



