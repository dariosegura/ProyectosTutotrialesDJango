from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
import datetime
from Projecto1.model.marca_carro import marca_carro

def saludo(request): #primera vista
    doc_externo=open("D:/Investigacion/Fodein/2021/SIGEPI/dJango/Tutoriales/ProyectosDJango/Projecto1/Projecto1/template/saludo.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)

def despedida(request): #segunda vista
    return HttpResponse("<h1 style='color:blue;'>Chao</h1>")

def get_fecha(request): #Tercer fecha
    fecha_actual=datetime.datetime.now()
    doc_externo=open("D:/Investigacion/Fodein/2021/SIGEPI/dJango/Tutoriales/ProyectosDJango/Projecto1/Projecto1/template/get_fecha.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({"fecha_actual":fecha_actual})
    documento=plt.render(ctx)
    return HttpResponse(documento)

def calculaedad(request, year, edadactual):
    fechaactual=datetime.datetime.now()
    documento="""
    <p>Edad actual: %s</p>
    <p>Para el año: %s</p>
    <p>Sería: %s</p>
    """ %(year,edadactual,(year-fechaactual.year)+edadactual)
    return HttpResponse(documento)

def get_marcas_carro(request):
    marcas=marca_carro.get_marcas()
    doc_externo=get_template("marca_carros.html")
    documento=doc_externo.render({"marcas":marcas})
    return HttpResponse(documento)