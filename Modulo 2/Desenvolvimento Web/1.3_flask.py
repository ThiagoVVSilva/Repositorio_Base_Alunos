from flask import Flask
app = Flask(__name__) # representa o nome do arquivo

@app.route('/')
def home():
   return "hello word"

@app.route('/sobre')
def sobre():
    return 'hello, my name is Thiago Vianna and i like walk :)'

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f'hello {nome} Seja bem-vindo(a)!'

if __name__ == '__main__':
    app.run(debug=True)