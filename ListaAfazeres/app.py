from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# 3 barras são caminhos relativos, 4 barras são caminhos absolutos

class Tarefa(db.Model):
        # Como funciona o modelo
        # Colunas ordenadas em inteiros são a nossa chave primária
        # O conteúdo de cada tarefa são strings de tamanho máximo 200 chars, e não podem ser nulas
        # Cada nota tem também a data de sua criação
        id = db.Column(db.Integer, primary_key = True)
        conteudo = db.Column(db.String(200), nullable = False)
        data_criacao = db.Column(db.DateTime, default = datetime.utcnow)

        # Qual = retorna qual tarefa estamos tratando
        # %r = representação de um objeto (novo ou ponteiro para existente)
        def __qual__(self):
                return '<Tarefa %r>' % self.id

@app.route('/', methods = ['POST', 'GET'])
def index():
        if request.method == 'POST':
                # Se estiver tentando submeter uma nova nota
                desc_tarefa = request.form['descricao']
                nova_tarefa = Tarefa(conteudo=desc_tarefa)

                try:
                        db.session.add(nova_tarefa)
                        db.session.commit()
                        return redirect('/index.html')
                except:
                        return 'Houve um erro ao adicionar sua tarefa'
        else:
                # Senão devolva o GET do index
                # Contendo as tarefas, tal que ordenadas pela data de criação para todas existentes
                todas_tarefas = Tarefa.query.order_by(Tarefa.data_criacao).all()
                return render_template('index.html', Tarefa = todas_tarefas)

if __name__ == "__main__":
        app.run(debug = True)