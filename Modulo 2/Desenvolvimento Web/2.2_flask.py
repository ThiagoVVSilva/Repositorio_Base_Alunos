# exercicio 2.2: links entre rotas
# add um menu de navegação simples com links para todas as suas rotas(/,/sobre,/saudacao,etc.)
# Passar a variavel atraves do 'url_for' dentro do script html: ("{{url_for('saudacao), nome='meu pai'}}")
# 'saudacao' é o nome da função python que define a rota
#nome="meu pai"est6á passando o valor para a variavel que a rota espera (<nome>)

from flask import Flask, render_template
app = Flask(__name__) # representa o nome do arquivo

@app.route('/')
def home():
   return render_template('ex_2-2.html')

@app.route('/sobre')
def sobre():
    return 'eu sou aluno da fabrica de garoto de programa'

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f'oie {nome} Seja bem-vindo(a)!'

@app.route('/dobro/<int:numero>')
def dobro(numero):
    return f'o dobro do {numero} é {2*numero}.'

if __name__ == '__main__':
    app.run(debug=True)