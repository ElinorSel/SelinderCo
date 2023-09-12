from flask import Flask, render_template, jsonify

#create an instance of flask "app" with the name being this filename
app = Flask(__name__)

JOBS = [{
    "id": 1,
    "title": "Senior Software Engineer",
    "location": "Stockholm, Sweden",
    "salary": "400 000kr"
}, {
    "id": 2,
    "title": "Marketing Manager",
    "location": "Seoul, South Korea",
    "salary": "300 000kr"
}, {
    "id": 3,
    "title": "Intern",
    "location": "Remote"
}]


@app.route(
    '/'
)  #define the url for this page / will give us just the default home page
def helloWorld():
  return render_template("home.html", jobs=JOBS)  #renderar den sidan du vill


@app.route('/api/jobs')
def listJobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(
      host="0.0.0.0", debug=True
  )  #runnar locally skriver detta bara eftersom flask har en annan run command än default här i replit
