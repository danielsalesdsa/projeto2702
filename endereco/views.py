from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
import requests 

from .models import Address
from .forms import AddressForm, CepForm

def cep_search_view(request):
    if request.method == 'GET':
        form = CepForm()

    message = ''

    if request.method == 'POST':
        form = CepForm(request.POST)

        cep_digitado = request.POST.get('cep')
        url = f"https://viacep.com.br/ws/{cep_digitado}/json/"
        response = requests.get(url)

        if response.status_code == 200:
            dados_cep = response.json()
            if 'erro' in dados_cep:
                message = 'CEP não encontrado'

            else: 
                reposta_em_json_filtrada = {
                    'cep': dados_cep['cep'],
                    'logradouro': dados_cep['logradouro'],
                    'bairro': dados_cep['bairro'],
                    'localidade': dados_cep['localidade'],
                    'uf': dados_cep['uf'],
                }
                form = CepForm(initial=reposta_em_json_filtrada)

                if form.is_valid():
                    form.save()
                
        else:
            message = "Erro durante a requisição a API"

    return render(request, 'endereco/cepSearch.html', {
        'form': form,
        'message': message
    })

class AddressCreate(CreateView):
    model = Address
    form_class = AddressForm
    context_object_name = 'CreateAddressForm'
    template_name = 'endereco/addressForm.html'
    success_url = reverse_lazy('endereco:list')

class AddressList(ListView):
    model = Address
    template_name = 'endereco/addressList.html'
    context_object_name = 'addressess'

class AddressUpdate(UpdateView):
    model = Address
    form_class = AddressForm
    context_object_name = 'address'
    template_name = 'endereco/addressForm.html'
    success_url = reverse_lazy('edndereco:listar')

class AddressDetail(DetailView):
    model = Address
    template_name = 'endereco/addressDetail.html'
    context_object_name = 'address'

class AddressDelete(DeleteView):
    model = Address
    template_name = 'endereco/addressDelete.html'
    success_url = reverse_lazy('endereco:listar')





# Create your views here.
