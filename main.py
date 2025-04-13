from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

usuario_login_page = {
    "email": "admin@admin",
    "senha": "admin"
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    mensagem = " "
    if request.method == 'POST':
        usuario = request.form.get('email')
        senha = request.form.get('senha')

        if usuario == usuario_login_page['email'] and senha == usuario_login_page['senha']:
            return redirect('https://www.youtube.com')
        
        elif usuario != usuario_login_page['email']:
            mensagem = "O e-mail está errado"
        
        elif senha != usuario_login_page['senha']:
            mensagem = "A senha está incorreta"
        
        else:
            mensagem = "senha ou email invalido"   

    return render_template('login.html', mensagem=mensagem)   

if __name__ == '__main__':
    app.run(debug=True)