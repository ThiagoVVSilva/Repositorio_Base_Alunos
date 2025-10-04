#instale flask
#exercicio 1.1: hello flask
#Criar um app Flask basico que exibe "hello word" na rota principal('/)

from flask import Flask
app = Flask(__name__) # representa o nome do arquivo

@app.route('/')
def home():
   return "hello word"

if __name__ == '__main__':
    app.run(debug=True)