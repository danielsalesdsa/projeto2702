from django import forms
from .models import Address

class CepForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['cep', 'logradouro', 'bairro', 'localidade', 'uf']
        labels = {
            'cep': 'CEP',
            'logradouro': 'Rua',
            'bairro': 'Bairro',
            'localidade': 'Cidade',
            'uf': 'UF',
        }

        widgets = {
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'localidade': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.TextInput(attrs={'class': 'form-control'}),
        }
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['cep', 'logradouro', 'bairro', 'localidade', 'uf']
        labels = {
            'cep': 'CEP',
            'logradouro': 'Rua',
            'bairro': 'Bairro',
            'localidade': 'Cidade',
            'uf': 'UF',
        }

        widgets = {
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'logradouro': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'localidade': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.TextInput(attrs={'class': 'form-control'}),
        }