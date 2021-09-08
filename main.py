from lifestore import *
from collections import Counter
from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template('login.html')

@app.route("/dash")
def dash():
#MAS VENDIDOS
    #creamos un diccionario con los productos ordenados de mayor a menor en ventas
    for producto in lifestore_sales:
        columna = [fila[1] for fila in lifestore_sales]
    vendidos=Counter(columna)
    ordenados=vendidos.most_common()
    #acomodamos el diccionario y la lista anidada de los nombres del producto para saber el nombre del prodcuto
    _vendido = [fila[0] for fila in ordenados]
    _number = [fila[0] for fila in lifestore_products]
    _name = [fila[1] for fila in lifestore_products]
    nombreprod=[]
    #comparamos el id de la lista de productos con el id del prodcuto más vendido y cuando coinciden guardar en una nueva lista el nombre del producto
    for producto in _vendido:
        for nombre in _number:
            if nombre == producto:
                nombreprod.append(_name[nombre-1])
                continue        
#BUSQUEDAS
    for busquedas in lifestore_searches:
        columna = [fila[1] for fila in lifestore_searches]
    busquedass=Counter(columna)
    ordenados=busquedass.most_common()
    _busquedas=[]
    _searchesnum = [fila[0] for fila in ordenados]
    _searchesveces = [fila[1] for fila in ordenados]
    for producto in _vendido:
        bandera=0
        for searche in _searchesnum:
            bandera=bandera+1
            if searche == producto:
                _busquedas.append(_searchesveces[bandera-1])
        continue 
#MENOS VENDIDOS
    _menos_vendidos = list(reversed(nombreprod))
    _menos_busquedad = list(reversed(_busquedas))
    return render_template('dash.html',ventas=nombreprod,ventas_menos=_menos_vendidos, _busquedas=_busquedas, _menos_busquedad=_menos_busquedad)



@app.route("/login",methods=['POST'])
def log():
    try:
        _usuario = str(request.form.get('usuario'))
        _contraseña = str(request.form.get('contraseña'))
        _usuarioin=str("Admin")
        _contraseñain= str("12345")

        if _usuario == _usuarioin and _contraseña == _contraseñain:
            print("in")
            return redirect(url_for('dash'))

        else:
            return render_template('login.html', alert='Tu contraseña o usuario es incorrecto')
    except:
        print("error")

if __name__ == "__main__":
    app.run()
    app.run(debug=True)

