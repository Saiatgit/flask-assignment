from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient("mongodb+srv://testuser:test123@cluster0.dsdgkln.mongodb.net/?appName=Cluster0")
db = client["testdb"]
collection = db["users"]


@app.route('/')
def home():
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']

        collection.insert_one({
            "name": name,
            "email": email
        })

        return redirect('/success')

    except Exception as e:
        return str(e)


@app.route('/success')
def success():
    return "Data submitted successfully"

if __name__ == "__main__":
    app.run(debug=True)