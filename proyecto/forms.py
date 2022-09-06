
from wtforms import Form
from wtforms import StringField, TextAreaField   #necesitamos importar todo esto

    #aqui el hace from wtforms.field.html5
from wtforms.fields import EmailField

                    #hiddenfield se usa para ocultar el campo del honeypot
from wtforms import HiddenField
from wtforms import validators

def length_honeypot(form,field):
    if len(field.data)> 0:
        #raise se usa para levantar nosotros mismos un error
        raise validators.ValidationError("el campo debe estar vacio")


class CommentForm(Form):
    username = StringField ("usuario", [validators.length(min=4, max=25, message="ingrese un usuario valido")]) 
    email = EmailField ("Correo electronico")

    
    comment = TextAreaField ("comentario")

    honeypot = HiddenField("", [])