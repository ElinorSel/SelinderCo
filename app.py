from flask import Flask, render_template, jsonify
from flask.templating import render_template_string
from database import load_jobs_from_db, load_job_from_db

#create an instance of flask "app" with the name being this filename
app = Flask(__name__)


@app.route(
    '/'
)  #define the url for this page / will give us just the default home page
def helloWorld():
  jobs = load_jobs_from_db()
  return render_template("home.html", jobs=jobs)  #renderar den sidan du vill


@app.route('/api/jobs')
def listJobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template("jobpage.html", job=job)


if __name__ == "__main__":
  app.run(
      host="0.0.0.0", debug=True
  )  #runnar locally skriver detta bara eftersom flask har en annan run command än default här i replit
