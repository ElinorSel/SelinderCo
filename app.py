from flask import Flask

#create an instance of flask "app" with the name being this filename
app = Flask(__name__)


@app.route('/') #define the url for this page / will give us just the default home page
def helloWorld():
   return"Hello world"

helloWorld()
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug = True)
