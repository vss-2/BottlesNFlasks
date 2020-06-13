# Lista de Afazeres

## Instalação
```python
pip3 install virtualenv flask flask-sqlalchemy

### Acessando virtual env
virtualenv environment

### Ativando virtual env
source environment/bin/activate

### Desativando virtual env
deactivate

### Ativando server
python3 app.py

### Iniciando banco de dados
# Inicie a environment, depois:
python3
from app import db
db.create_all()
```

#### Baseado nesse vídeo do [FreeCodeCamp](https://www.youtube.com/watch?v=Z1RJmh_OqeA)