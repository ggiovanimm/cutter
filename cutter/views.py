from django.shortcuts import render
from .forms import CutterForm
from .models import Cutter

from django.shortcuts import render
from .forms import CutterForm
from .models import Cutter

def gerar_cutter(request):
    titulo = None
    debug_info = []
    if request.method == 'POST':
        form = CutterForm(request.POST)
        if form.is_valid():
            autoria = form.cleaned_data['autoria']
            normalized_autoria = autoria.strip().lower()
            
            # Busca exata
            cutter_obj = Cutter.objects.filter(autoria__iexact=normalized_autoria).first()
            if cutter_obj:
                titulo = cutter_obj.titulo
                # Adicionando a formatação também para correspondências exatas
                prefixo = cutter_obj.autoria[0].upper()
                cutter_formatado = f"{prefixo}{titulo}"
                debug_info.append(f"Correspondência exata encontrada: {cutter_obj.autoria} - {cutter_formatado}")
            else:
                # Busca pelo prefixo mais longo e apropriado
                best_match = None
                for i in range(1, len(normalized_autoria) + 1):
                    prefix = normalized_autoria[:i]
                    matches = Cutter.objects.filter(autoria__istartswith=prefix).order_by('-autoria')
                    for match in matches:
                        if match.autoria.lower() <= normalized_autoria:
                            if best_match != match:  # Evita adicionar o mesmo candidato repetidamente
                                best_match = match
                            break
                    if best_match:
                        if i == len(normalized_autoria) or normalized_autoria[i:i+1] > best_match.autoria[i:i+1]:
                            break
                
                if best_match:
                    titulo = best_match.titulo
                    prefixo = best_match.autoria[0].upper()
                    cutter_formatado = f"{prefixo}{best_match.titulo}"
                    debug_info.append(f"Prefixo encontrado: {best_match.autoria} - {cutter_formatado}")
                else:
                    titulo = "Autoria não encontrada."
                    cutter_formatado = titulo
    else:
        form = CutterForm()
        cutter_formatado = None
    
    return render(request, 'cutter/forms.html', {
        'form': form, 
        'titulo': cutter_formatado if 'cutter_formatado' in locals() else titulo, 
        'debug_info': debug_info
    })
    

def limpa_cutter(request):
    form = CutterForm()  # Reinicializa o formulário vazio
    titulo = None  # Limpa o título gerado
    debug_info = []  # Adiciona info de debug (opcional)
    
    return render(request, 'cutter/forms.html', {'form': form, 'titulo': titulo, 'debug_info': debug_info})
