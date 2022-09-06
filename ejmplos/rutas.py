from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")  
def hello():
 return 'Hello, estoy aprendiendo algo!'  


@app.route("/params")
@app.route("/params/<name>/")  
@app.route("/params/<name>/<int:num>")  
def params(name = "este es un valor por defecto", num = "nada"):
    return "el parametro es: {} {} ".format(name, num)



if __name__ == "__main__":
 app.run(debug = True, port = 8000) 

