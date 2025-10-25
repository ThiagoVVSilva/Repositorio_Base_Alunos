from flask import Flask, render_template, request, jsonify,redirect, url_for
from datetime import datetime
import json
import resend

resend.api_key = 're_gwhRoTkr_FnWS8p4m5L1iFGs7GYAzdrH8'

app= Flask(__name__)

with open('dados.json','r',encoding='utf-8') as arquivo:
    dados= json.load(arquivo)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        nome=request.form['name']
        email=request.form['email']
        mensagem=request.form['message']

        dados_mensagem = {
            'nome' :nome,
            'email' :email,
            'mensagem' :mensagem,
            'data' :f'{datetime.today()}'
        }

        dados.append(dados_mensagem)
        with open('dados.json','w',encoding='utf-8') as arquivo:
            json.dump(dados,arquivo,indent=4,ensure_ascii=False)
            
        r = resend.Emails.send({
                "from": "onboarding@resend.dev",
                "to": "thiagoviannavitalsilva@gmail.com",
                "subject": f"Solicitação de Adoção {nome}",
                "html": f"<p>Email:{email}<br>{mensagem}</p>"
                                  })
        return redirect(url_for('index'))#possivel erro
    
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)
  
 
  
  


        













