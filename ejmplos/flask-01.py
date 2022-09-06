from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")  
def hello():
 return 'Hello, estoy aprendiendo algo!'  


@app.route("/params")  
def params():
    param = request.args.get("params1", "no contiene ningun parametro")
    return "el parametro es: {}".format(param)



if __name__ == "__main__":
 app.run(debug = True, port = 8000) 





 #http://127.0.0.1:8000/params?params1=roberto