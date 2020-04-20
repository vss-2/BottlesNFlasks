import os
from bottle import template, route, run, get

@get('/')
def index():
        mensagem = 'Olá Vitor!'
        ## mensagem = os.environ.get('MSG_HOMEPAGE')
        return template('{{!msg}}', msg=mensagem)

run(host='localhost', port=8080, debug=True)
