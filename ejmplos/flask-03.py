#Forma combinada y cadena de consulta
# Flask también permite el acceso a un CombinedMultiDict que da acceso a los atributos
# request.form y request.args bajo una variable.
# Este ejemplo extrae datos de un name campo de formulario enviado junto con el campo de echo en
# la cadena de consulta.


from flask import Flask, request

app = Flask(import_name = __name__)

@app.route("/echo",methods=["POST"])

def echo():
    name = request.values.get("name", "no existe")
    to_echo = request.values.get("echo", "no funciona")
    response = "Hola {} como estas {}".format(name, to_echo)
    return response

if __name__ == "__main__":
    app.run()