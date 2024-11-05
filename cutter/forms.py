from django import forms
from .models import Cutter

class CutterForm(forms.ModelForm):
    class Meta:
        model = Cutter
        fields = ['autoria']
        widgets = {
            'autoria': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Sobrenome, Nome. Ex.: Cutter, Charles Ammi'
            }),
            # 'titulo': forms.TextInput(attrs={
                # 'class': 'form-control', 
                # 'placeholder': 'Ex.: Expansive classification'
            # }),
        }

        labels = {
            'autoria': 'Autoria da obra (Sobrenome, Nome)',  # Definir o rótulo para 'Autoria'
        }

    # def buscar_autoria(self):
    #     # Obtém a autoria do campo de entrada
    #     autoria_input = self.cleaned_data.get('autoria')
        
    #     # Filtra as autorias que contêm a substring (por exemplo, "Men")
    #     if autoria_input:
    #         return Cutter.objects.filter(autoria__icontains=autoria_input)
        
    #     return Cutter.objects.none()  # Retorna um queryset vazio se não houver entrada
