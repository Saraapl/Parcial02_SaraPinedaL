from flask import Flask, jsonify

app = Flask(__name__)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

@app.route('/<int:n>', methods=['GET'])
def procesar_numero(n):
    fact = factorial(n)
    etiqueta = "par" if fact % 2 == 0 else "impar"
    
    respuesta = {
        "numero": n,
        "factorial": fact,
        "etiqueta": etiqueta
    }
    
    return jsonify(respuesta)

@app.route('/')
def inicio():
    return "Bienvenido. Usa la URL /<número> para calcular el factorial."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
