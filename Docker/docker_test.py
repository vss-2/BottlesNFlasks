import os
from bottle import route, run, get

@get('/')
def index():
    mensagem = os.environ.get('MSG_HOMEPAGE')
	return mensagem

run(host='localhost', port=8080, debug=True)
