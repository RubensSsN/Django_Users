from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .forms import PessoaForm
from .models import Pessoa


class ListaPessoaView(ListView):
    model = Pessoa
    queryset: Pessoa.objects.all().order_by('ativa')
    

class CreatePessoaView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'


