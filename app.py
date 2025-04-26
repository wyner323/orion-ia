from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def buscar_produto(nome_produto):
    conn = sqlite3.connect('database/orion.db')
    cursor = conn.cursor()
    cursor.execute("SELECT localizacao FROM produtos WHERE nome LIKE ?", ('%' + nome_produto + '%',))
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado else None

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    erro = None
    if request.method == 'POST':
        produto = request.form['produto']
        resultado = buscar_produto(produto)
        if not resultado:
            erro = "Produto não encontrado."
    return render_template('index.html', resultado=resultado, erro=erro)

if __name__ == '__main__':
    app.run(debug=True)
