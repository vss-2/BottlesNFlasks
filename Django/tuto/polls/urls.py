from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
	path('', views.index, name='home'),
	path('<int:question_id>/', views.detail, name='detail'),
	path('<int:question_id>/results/', views.results, name='results'),
	path('<int:question_id>/vote/', views.vote, name='vote'),
]
# Descritos os caminhos e detalhes
# das telas que estão views
# Para acessar, por exemplo: é /polls/1/results