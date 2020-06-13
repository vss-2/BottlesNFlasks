from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from http.client import HTTPException

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

        # Esta função existia anteriormente no SQLAlchemy
        # em resumo, ela apenas trata exceção de não encontrado no banco
        def det_or_404(id):
                busca = db.Query.get_or_404(id)
                if busca != None:
                        return busca
                else:
                        return HTTPException(code=404)

@app.route('/', methods = ['POST', 'GET'])
def index():
        if request.method == 'POST':
                # Se estiver tentando submeter uma nova nota
                desc_tarefa = request.form['descricao']
                nova_tarefa = Tarefa(conteudo=desc_tarefa)

                try:
                        db.session.add(nova_tarefa)
                        db.session.commit()
                        return redirect('/')
                except:
                        return 'Houve um erro ao adicionar sua tarefa'
        else:
                # Senão devolva o GET do index
                # Contendo as tarefas, tal que ordenadas pela data de criação para todas existentes
                todas_tarefas = Tarefa.query.order_by(Tarefa.data_criacao).all()
                return render_template('index.html', todas_tarefas = todas_tarefas)

@app.route('/deletar/<int:id>')
def deletar(id):
        # Não há methods pois não existe tela de deletar, apenas solicitação
        # Vai ver a tarefa no db e mover o ponteiro para ela pegando seu id,
        # caso a tarefa não seja encontrada, retorna erro 404
        tarefa_apagar = Tarefa.query.get_or_404(id)
        try:
                db.session.delete(tarefa_apagar)
                db.session.commit()
                return redirect('/')
        except:
                'Houve um problema ao remover a tarefa, ela não foi encontrada no banco!'
        

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def editar(id):
        tarefa_editar = Tarefa.query.get_or_404(id)

        if request.method == 'POST':
                # Você editou o conteúdo, tenho que novamente adicioná-lo ao db
                tarefa_editar.conteudo = request.form['conteudo']

                try:
                        db.session.commit()
                        return redirect('/')
                except:
                        return 'Houve um erro ao atualizar sua tarefa!'
        
        else:
                # Você apenas está na tela de edição
                return render_template('edit.html', tarefa = tarefa_editar)


if __name__ == "__main__":
        app.run(debug = True)