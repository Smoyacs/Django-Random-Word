from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    
    if "count_session" not in request.session.keys():
        print ("Bienvenido por primera vez")
        request.session['count_session'] = 0
        
    else:
        print ("generando palabras")
        request.session['count_session'] += 1
        
    context = {
        "count_session": request.session['count_session'],
        "rand_word": get_random_string(length=14)
    }
    
    return render(request, 'index.html', context)

def reset(request):
    print ("Reset")
    del request.session['count_session'] # elimina la sesion provocando que al visitar la pagina los intentos se establezcan en 0 y no en 1
    
    return redirect('/random_word')