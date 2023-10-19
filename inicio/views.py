from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse 
from datetime import datetime
from inicio.models import Curso

datos = {
    'fecha': datetime.now()
}
def inicio(request):  
    #archivo = open (r'inicio\templates\inicio\inicio.html', 'r')    
    #template = Template(archivo.read())    
    #archivo.close()    
    #contexto = Context(datos)    
    #template_renderizado = template.render(contexto)    
    #return HttpResponse(template_renderizado) 
    
    return render(request, r'inicio\inicio.html', datos)

def crear_curso(request, titulo, numero):
    
    curso = Curso(titulo=titulo, numero=numero)
    curso.save()
    
    return render(request, r'inicio\curso_creado.html', {})
    
    