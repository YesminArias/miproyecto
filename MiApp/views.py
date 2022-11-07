from django.shortcuts import render

# Create your views here.
from MiApp.models import Family

def mostrar_familia(request):
    
    familiar1 = Family(nombre='Sonia Socorro Esparza', edad=62,fechaNacimiento='1960-01-13')
    familiar2 = Family(nombre='Antonio Arias Perez', edad=80,fechaNacimiento='1942-09-04')
    familiar3 = Family(nombre='Briany Valeria Molina Arias', edad=6,fechaNacimiento='2016-04-09')
    familiar4 = Family(nombre='Jhon Edison Arias Esparza', edad=35,fechaNacimiento='1987-08-30')
    
    return render(request, 'MiApp/Templetes/MiApp/familia.html', {'familia': [familiar1, familiar2, familiar3, familiar4]})