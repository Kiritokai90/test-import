from flask import Flask

Flask_App = Flask(__name__)

@app.route("/")
def acceuil():
  return "cc"


app.run(host="0.0.0.0", port=8080)

