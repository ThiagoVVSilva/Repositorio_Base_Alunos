# Exercicio validaçao basica de campos 
# implementar uma verificação no formulario anterior
# para garantir que os valores sejam numeros antes da soma-los

from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        try:
            num1 = int(request.form['num1'])
            num2 = int(request.form['num2'])
            resultado = num1 + num2
            return render_template('ex_4-3.html',resultado=resultado)
        except:
            erro = 'Por favor apenas digite numeros validos.'
            return render_template('ex_4-3.html', erro=erro)
    return render_template('ex_4-3.html')




if __name__ == '__main__':
    app.run(debug=True)