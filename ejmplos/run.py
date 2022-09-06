from flask import Flask
app = Flask(__name__)   #nuevo objeto

@app.route('/')  #wrap o un decorador
def hello():
 return 'Hello, estoy aprendiendo algo!'  #regresa un string



if __name__ == '__main__':

    #con debug True hacemos que este a la escuche y aplique cualquier cambio en el servidor
 app.run(debug = True, port = 8000) 