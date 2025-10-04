#estrutura de controle
#passe uma lista de nomes para o template e use um for em jinja para listar todos os nomes em um <ul>
from flask import Flask, render_template
app = Flask(__name__) # representa o nome do arquivo

@app.route('/')
def home():
   return 'Hello flask'

@app.route('/sobre')
def index():
    return 'eu sou aluno da fabrica de garoto de programa'

@app.route('/lista')
def lista():
    alunos = ['kauan','Luana','Miguel','Thiago','alexsandra']
    return render_template('ex_3-2.html',lista=alunos)


if __name__ == '__main__':
    app.run(debug=True)