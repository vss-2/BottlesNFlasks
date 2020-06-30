from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Question

def index(request):
	ultima_questao_lista = Question.objects.order_by('data_publicacao')[:5]
	template = loader.get_template('polls/index.html')
	context = {
		'ultima_quest_lista': ultima_questao_lista,
	}
	return HttpResponse(template.render(context, request))

def detail(request, question_id):
	return HttpResponse('Visualizando a votação de: %s' %question_id)

def results(request, question_id):
	resultado = 'Você está olhando o resultado da votação de: %s'
	return HttpResponse(resultado % question_id)

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		escolhida = question.txt_pergunta.get(pk=request.POST['escolha'])
	except:
		# Exibir o formulário de votação
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': 'Você não selecionou todas as partidas!'
		})
	else:
		escolhida += 1
		escolhida.save()
		# Sempre retorna uma HttpResponseRedirect depois de operação
		# de POST obter sucesso. Isso previne que o dado seja enviado 
		# duas vezes, caso usuário pressione botão voltar.
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))