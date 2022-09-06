
from flask import Flask, render_template

app = Flask(__name__)

#por defecto para llamar a una urel se usa el metodo get para usar post lo hacemos asi

@app.route("/cliente")
def todos_clientes():
    return "Devuelve listado de clientes"



@app.route("/cliente/<int:id>")
def obtener_cliente(id):
    return "devuelve un cliente"



@app.route("/cliente", methods=["POST"])
def crear_clientes():
    return "Cliente guardado"


@app.route("/cliente/<int:id>", methods=["DELETE"])
def eliminar_clientes(id):
    return "Cliente eliminado"








@app.route("/")
def index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)