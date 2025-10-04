# exercicio 3.1: Templates com variaveis
#modifique o templete para receber o nome como variavel e exibir "Bem vindo",{{nome}}
from flask import Flask, render_template
app = Flask(__name__) # representa o nome do arquivo

@app.route('/')
def index():
   return 'hello flask'

@app.route('/sobre')
def sobre():
    return 'eu sou aluno da fabrica de garoto de programa'

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return render_template('ex_3-1.html',nome=nome)

if __name__ == '__main__':
    app.run(debug=True)