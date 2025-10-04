#Exercicio 4.1: formulario simples com request form
# Crie uma pagina com um formulario que envie em nome e retorna uma saudação personalizada com esse nome

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        nome = request.form['nome']
        return f'Ola {nome}, seja bem vindo a fabrica de programadores.'
    return render_template('ex_4-1.html')

if __name__ == '__main__':
    app.run(debug=True)