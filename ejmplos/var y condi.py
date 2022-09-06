from flask import Flask
                #nos permite renderizar
from flask import render_template
app = Flask(__name__)

@app.route("/user/<name>")
def user(name="roberto"):
    edad = 42
    mi_list = [1,2,3,4,5,6,7,8,9,10,"alto"]
    return render_template("user.html", name= name, edad= edad, list= mi_list)

if __name__ == "__main__":
    app.run(debug = True, port=8000)