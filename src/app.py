
from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
     return "Hello,World, this is pipetesting demo! New Changes made"

if __name__== "__main__":
     app.run()


