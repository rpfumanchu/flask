from flask import Flask
from flask import request

app = Flask(import_name = __name__)
@app.route("/echo")
def echo ():

    to_echo = request.args.get("echo", "no contiene ningun parametro")
    response = "{}".format(to_echo)
    return response

if __name__ == "__main__":
    app.run()