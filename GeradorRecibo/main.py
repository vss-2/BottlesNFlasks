import os
from flask import Flask, render_template, url_for, redirect
from datetime import datetime
from flask_sqlachemy import SQLAlchemy

app = Flash(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Recibo(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        data_criacao = db.Column(db.Datetime, default = datetime.utcnow)
        texto     = db.Column(db.String(2000), nullable = False)
        data      = db.Column(db.Datetime, nullable = False)
        pagador   = db.Column(db.String(100), nullable = False)
        recebedor = db.Column(db.String(100), nullable = False)
        valor     = db.Column(db.Float, nullable = False)
        local     = db.Column(db.String(100), nullable = False)

        def __id__(self):
                return '<Recibo %r>' % self.id

@app.route('/', method = ['GET', 'POST'])
def index():
        if request.method == 'POST':
                txt_recibo = request.form['texto']
                pag_recibo = request.form['pagador']
                rec_recibo = request.form['recebedor']
                dat_recibo = request.form['data']
                loc_recibo = request.form['local']
                val_recibo = request.form['valor']
                novo_recibo = Recibo(
                try:
                        db.session.add('''
                                texto     = txt_recibo,
                                data      = dat_recibo,
                                pagador   = pag_recibo,
                                recebedor = rec_recibo,
                                valor     = val_recibo,
                                local     = loc_recibo
                                ''')
                        db.session.commit()
                        return redirect('/')
                except:
                        return 'Houve um erro'
        else: 
                todos_recibos = Recibo.query.order_by(Recibo.data_criacao).all()
                return render_template('index.html', Recibo = todos_recibos)

if __name__ == "__main__":
        app.run(debug = True)