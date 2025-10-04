# Exercicio: condicionais em templates
# crie uma rota que envia uma idade e, no templete, use if para mostrar uma mensagem
#diferente
from flask import Flask, render_template
app = Flask(__name__) # representa o nome do arquivo

@app.route('/')
def home():
   return 'Hello flask'

@app.route('/sobre')
def index():
    return 'eu sou aluno da fabrica de garoto de programa'

@app.route('/idade/<int:idade>')
def idade(idade):
    return render_template('ex_3-3.html',idade=idade)


if __name__ == '__main__':
    app.run(debug=True)