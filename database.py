#connect to db using sql alchemy lib
from flask.templating import stream_template_string
from sqlalchemy import create_engine, text, insert
import os

db_connection_str = os.environ["DB_CONNECTION_STRING"]
engine = create_engine(db_connection_str,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._mapping)
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    text_str = "SELECT * FROM jobs WHERE id = " + str(id)
    result = conn.execute(text(text_str))
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._mapping


def add_application_to_db(job_id, data):

  with engine.connect() as conn:
    text_str = "INSERT INTO `selinderco`.`applications` (`job_id`, `full_name`, `email`, `linkedin`, `education`, `work_experience`, `resume_url`) VALUES( "

    second_str = "'" + job_id + "',  '" + data['full_name'] + "',  '" + data[
        'email'] + "',  '" + data['linkedin'] + "',  '" + data[
            'education'] + "',  '" + data['work_experience'] + "',  ';" + data[
                'resume_url'] + "')"

    full_string = text_str + second_str

    query = text(full_string)
    conn.execute(query)
