import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):

        def __str__(self):
                return self.txt_pergunta
        # Adicionamos o esta def para quando perguntarmos ao
        # banco de dados ele responder algo diferente de 'Question object'

        def bool_foi_pub_hoje(self):
                return self.data_publicacao >= timezone.now() - datetime.timedelta(days=1)

        txt_pergunta    = models.CharField(max_length=200)
        data_publicacao = models.DateTimeField('date published')
        # O primeiro parâmetro "date published" é para 
        # tornar legível e mais fácil documentação

class Choice(models.Model):

        def __str__(self):
                return self.escolha

        pergunta = models.ForeignKey(Question, on_delete=models.CASCADE)
        escolha  = models.CharField(max_length=200)
        time_1   = models.CharField(max_length=5)
        time_2   = models.CharField(max_length=5)
        time_3   = models.CharField(max_length=5)
        time_4   = models.CharField(max_length=5)
        votos    = models.IntegerField(default=0)
        # A foreign key é usada para os tipos de relacionamentos
        # Muitos para um, muitos para muitos e um para um