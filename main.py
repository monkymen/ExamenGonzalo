from flask import Flask, render_template, request

app = Flask(__name__)

PRECIO_TARRO = 9000

USUARIOS = {
    "juan": {"password": "admin", "rol": "Administrador"},
    "pepe": {"password": "user", "rol": "Usuario"},
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    nombre = None
    total_sin_descuento = None
    descuento = None
    total_a_pagar = None

    if request.method == "POST":
        nombre = request.form["nombre"].strip()
        edad = int(request.form["edad"])
        cantidad = int(request.form["cantidad"])

        total_sin_descuento = cantidad * PRECIO_TARRO

        if 18 <= edad <= 30:
            porcentaje_descuento = 0.15
        elif edad > 30:
            porcentaje_descuento = 0.25
        else:
            porcentaje_descuento = 0.0

        descuento = total_sin_descuento * porcentaje_descuento
        total_a_pagar = total_sin_descuento - descuento

    return render_template(
        "ejercicio1.html",
        nombre=nombre,
        total_sin_descuento=total_sin_descuento,
        descuento=descuento,
        total_a_pagar=total_a_pagar,
    )


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = None

    if request.method == "POST":
        nombre = request.form["nombre"].strip()
        contrasena = request.form["contrasena"]

        usuario = USUARIOS.get(nombre)
        if usuario and usuario["password"] == contrasena:
            mensaje = f"Bienvenido {usuario['rol']} {nombre}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template("ejercicio2.html", mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True)
