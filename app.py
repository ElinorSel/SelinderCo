from flask import Flask, render_template

#create an instance of flask "app" with the name being this filename
app = Flask(__name__)


@app.route(
    '/'
)  #define the url for this page / will give us just the default home page
def helloWorld():
  return render_template("home.html")  #renderar den sidan du vill


if __name__ == "__main__":
  app.run(
      host="0.0.0.0", debug=True
  )  #runnar locally skriver detta bara eftersom flask har en annan run command än default här i replit
