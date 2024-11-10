from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Eventos, Testimonios, Adopta
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import TestimoniosForm, DonaForm



def pagina_principal(request):
    _Eventos = Eventos.objects.all()
    
    return render(request, 'index.html',{
        'Eventos': _Eventos
    })


def pagina_who(request):
    return render(request, 'who.html')



def pagina_testimonios(request):
    _Testimonios = Testimonios.objects.all()
    return render(request, 'Testimonios.html',{
        'Testimonios': _Testimonios
    })



def pagina_adopta(request):
    _adopta = Adopta.objects.all()
    return render(request, 'Adopta.html',{
        'adoptados': _adopta
    })
    
@login_required    
def pagina_indexautenticado(request):
    return render(request, 'indexAutenticado.html')
    
    
    
def pagina_registro(request):
    
    if request.method == 'GET':    
        return render(request, 'Registrate.html',{
            'form': UserCreationForm()
        })
        
    else: 
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect ('index')
            except IntegrityError:
                    return render(request, 'Registrate.html',{
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
            except:
                  return render(request, 'Registrate.html',{
                    'form': UserCreationForm,
                    'error': 'Ups Algo paso intentalo de nuevo'
                })
      
        return render(request, 'Registrate.html',{
            'form': UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })



def pagina_exit(request):
    logout(request)
    return redirect('ingresar')



def pagina_ingresar(request):
       
    if request.method == 'GET':
        return render(request, 'ingresar.html',{
            'form': AuthenticationForm
        })
        
    else: 
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'ingresar.html',{
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else: 
            login(request, user) 
            return render(request,'indexautenticado.html',{
                'user': user
            })

@login_required
def testimonios(request):
    if request.method == 'GET':
        return render(request, 'testimonio.html',{
        'form': TestimoniosForm
        })
    else:
        try:
            FORM = TestimoniosForm(request.POST)
            donacionn = FORM.save(commit=False)
            donacionn.save()
            _Testimonios = Testimonios.objects.all()
            return render(request, 'Testimonios.html',{
                'Testimonios': _Testimonios
            })
                 
        except ValueError:
            return render(request, 'testimonio.html',{
                'form': TestimoniosForm,
                'error': 'Digita correctamente los datos'
            }) 
        except:
            
            return render(request, 'testimonio.html',{
                'form': TestimoniosForm,
                'error': 'Ups algo paso intentalo de nuevo'
            }) 
        
    
    
@login_required
def donacion(request):
    if request.method == 'GET':
        return render(request, 'donacion.html',{
        'form': DonaForm
        })              
    else:
        try:
            FORM = DonaForm(request.POST)
            donacionn = FORM.save(commit=False)
            donacionn.USER = request.user
            donacionn.save()
            return render(request,'indexautenticado.html',{
                    'user': request.user
                })
                 
        except ValueError:
            return render(request, 'donacion.html',{
                'form': DonaForm,
                'error': 'Digita correctamente los datos'
            }) 
        except:
            
            return render(request, 'donacion.html',{
                'form': DonaForm,
                'error': 'Ups algo paso intentalo de nuevo'
            }) 

    


