"""
Aplicación Flask para una calculadora web.
"""

import os

from flask import Flask, render_template, request

from .calculadora import sumar, restar, multiplicar, dividir

app = Flask(__name__)
app_port = int(os.environ.get("PORT", 5000))


@app.route("/", methods=["GET", "POST"])
def index():
    """Maneja la lógica de la calculadora y renderiza la plantilla."""
    resultado = None
    ### test error

    if request.method == "POST":
        try:
            #test

            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
             #test

            operacion = request.form["operacion"]
             #test
            if operacion == "sumar":
                resultado = sumar(num1, num2)
            elif operacion == "restar":
                resultado = restar(num1, num2)
            elif operacion == "multiplicar":
                resultado = multiplicar(num1, num2)
            elif operacion == "dividir":
                resultado = dividir(num1, num2)
            else:
                 #test
                resultado = "Operación no válida"
        except ValueError:
            resultado = "Error: Introduce números válidos"
        except ZeroDivisionError:
            resultado = "Error: No se puede dividir por cero"

    return render_template("index.html", resultado=resultado)


@app.route("/health")
def health():
    """Endpoint de salud para verificar que la aplicación está funcionando."""
    return "OK", 200


if __name__ == "__main__":
    app.run(debug=False, port=app_port, host="0.0.0.0")
