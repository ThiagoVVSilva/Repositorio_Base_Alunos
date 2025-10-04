#exercicio 2.1:html basico na resposta
#modificar sua rota principal para retornar um pequeno html com titulo,
#paragrafo e um link para outra rota.
#usar 'rende_template' para renderizar um arquivo .html
# usar 'url_for()' nas anchor tags no script html

from flask import Flask, render_template
app = Flask(__name__) # representa o nome do arquivo

@app.route('/')
def home():
   return render_template('ex_2-1.html')

@app.route('/sobre')
def sobre():
    return 'Fabrica de programadores'

@app.route('/zezinho')
def zezinho():
    return 'Achou a rota'

if __name__ == '__main__':
    app.run(debug=True)