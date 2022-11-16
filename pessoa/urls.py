from django.urls import path

from .views import ListaPessoaView, CreatePessoaView

urlpatterns = [
    path('', ListaPessoaView.as_view(), name='pessoa.index'),
    path('create/', CreatePessoaView.as_view(), name='pessoa.create')
]
