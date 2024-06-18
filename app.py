from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "Id": 1,
        "Title": "Data Analyst",
        "Location": "Bengaluru, India",
        "Salary": "Rs. 10,00,000",
    },
    {
        "Id": 2,
        "Title": "Data Scientist",
        "Location": "Bengaluru, India",
        "Salary": "",
    },
    {
        "Id": 3,
        "Title": "Frontend Engineer",
        "Location": "Bengaluru, India",
        "Salary": "Rs. 10,00,000",
    },
    {
        "Id": 4,
        "Title": "Data-Science Intern",
        "Location": "Remote",
        "Salary": "Rs. 4,00,000",
    }
]


@app.route("/")
def hello_world():
    return render_template("hello.html", jobs=JOBS, company_name='Demon Slayer')

# This is for viewing the data in the jason forms:
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)