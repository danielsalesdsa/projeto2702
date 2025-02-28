from django.urls import path
from .views import AddressCreate, AddressList, AddressUpdate, AddressDetail, AddressDelete, cep_search_view

app_name = 'endereco'

urlpatterns = [
    path('cep/', cep_search_view, name='cep'),


    path('criar/', AddressCreate.as_view(), name='criar'),
    path('listar/', AddressList.as_view(), name='listar'),
    path('detalhes/<int:pk>', AddressDetail.as_view(), name="detalhar"),
    path('editar/<int:pk>', AddressUpdate.as_view(), name="atualizar"),
    path('deletar/<int:pk>', AddressDelete.as_view(), name="deletar"),
    
]