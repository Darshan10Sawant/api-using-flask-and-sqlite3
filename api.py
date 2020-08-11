from flask import Flask

app=Flask(__name__)
app.config["DEBUG"]=True

@app.route('/', methods=['GET'])
def home():
    return "<center><h1>Distance reading archive</h1><p><u>This site is a prototype API for distant reading of science fiction novels.</uh></p></center>"

app.run()