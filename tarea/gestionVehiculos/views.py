from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Propietario, Vehiculo, Registro

def index(request):
    propietarios = Propietario.objects.all()
    return render(request, 'gestionVehiculos/index.html', {'propietarios': propietarios})

def registrar_entrada(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)

    if request.method == "POST":
        Registro.objects.create(
            vehiculo=vehiculo,
            fecha_hora_entrada=timezone.now()
        )
        return redirect('index') 

    return render(request, 'gestionVehiculos/registrar_entrada.html', {'vehiculo': vehiculo})

def registrar_salida(request, registro_id):
    registro = get_object_or_404(Registro, id=registro_id)

    if request.method == "POST":
        registro.fecha_hora_salida = timezone.now()  
        registro.save()
        return redirect('index') 

    return render(request, 'gestionVehiculos/registrar_salida.html', {'registro': registro})


def registrar_propietario(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        numero_apartamento = request.POST['numero_apartamento']
        telefono = request.POST['telefono']
        email = request.POST['email']
        
        if not Propietario.objects.filter(email=email).exists():
            Propietario.objects.create(
                nombre=nombre,
                numero_apartamento=numero_apartamento,
                telefono=telefono,
                email=email
            )
            return redirect('index')
        else:
            pass  

    return render(request, 'gestionVehiculos/registrar_propietario.html')

def editar_propietario(request, propietario_id):
    propietario = get_object_or_404(Propietario, id=propietario_id)
    if request.method == "POST":
        propietario.nombre = request.POST.get('nombre')
        propietario.numero_apartamento = request.POST.get('numero_apartamento')
        propietario.telefono = request.POST.get('telefono')
        propietario.email = request.POST.get('email')
        propietario.save()
        return redirect('index')
    return render(request, 'gestionVehiculos/editar_propietario.html', {'propietario': propietario})

def eliminar_propietario(request, propietario_id):
    propietario = get_object_or_404(Propietario, id=propietario_id)
    propietario.delete()
    return redirect('index')

def registrar_vehiculo(request, propietario_id):
    propietario = get_object_or_404(Propietario, id=propietario_id)
    
    if request.method == "POST":
        matricula = request.POST['matricula']
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        color = request.POST['color']
        
        Vehiculo.objects.create(
            propietario=propietario,
            matricula=matricula,
            marca=marca,
            modelo=modelo,
            color=color
        )
        
        return redirect('index')  

    return render(request, 'gestionVehiculos/registrar_vehiculo.html', {'propietario': propietario})

def listar_vehiculos(request, propietario_id):
    propietario = get_object_or_404(Propietario, id=propietario_id)
    vehiculos = propietario.vehiculos.all()
    return render(request, 'gestionVehiculos/listar_vehiculos.html', {'propietario': propietario, 'vehiculos': vehiculos})

def editar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    
    if request.method == "POST":
        vehiculo.matricula = request.POST.get('matricula')
        vehiculo.marca = request.POST.get('marca')
        vehiculo.modelo = request.POST.get('modelo')
        vehiculo.color = request.POST.get('color')
        vehiculo.save()
        return redirect('listar_vehiculos', propietario_id=vehiculo.propietario.id)
    
    return render(request, 'gestionVehiculos/editar_vehiculo.html', {'vehiculo': vehiculo})

def eliminar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    propietario_id = vehiculo.propietario.id
    vehiculo.delete()
    return redirect('listar_vehiculos', propietario_id=propietario_id)

def registrar_entrada(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    
    Registro.objects.create(
        vehiculo=vehiculo,
        fecha_hora_entrada=timezone.now()
    )
    
    return redirect('index')  
def registrar_salida(request, registro_id):
    registro = get_object_or_404(Registro, id=registro_id)
    
    if request.method == "POST":
        registro.fecha_hora_salida = timezone.now()  
        registro.save()
        return redirect('index')  
    
    return render(request, 'gestionVehiculos/registrar_salida.html', {'registro': registro})


def listar_registros(request):
    registros = Registro.objects.all()
    return render(request, 'gestionVehiculos/listar_registros.html', {'registros': registros})

def historial_registro(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    registros = Registro.objects.filter(vehiculo=vehiculo).order_by('-fecha_hora_entrada')
    return render(request, 'gestionVehiculos/historial_registro.html', {'vehiculo': vehiculo, 'registros': registros})


