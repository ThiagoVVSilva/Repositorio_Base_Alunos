#exercicio 2:rota personalizada
#adicione uma nova rota '/sobre' que retorna uma mensagem com seu nome
# e uma frase sobre vc

from flask import Flask
app = Flask(__name__) # representa o nome do arquivo

@app.route('/')
def home():
   return "hello word"

@app.route('/sobre')
def sobre():
    return 'hello, my name is Thiago Vianna and i like walk :)'

if __name__ == '__main__':
    app.run(debug=True)