from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def index(request, pagina):
	if request.method == 'GET':
		try:
			listado = Pages.objects.get(name=pagina)
		except Pages.DoesNotExist:
			return HttpResponse('Lo sentimos, esta pagina no ha sido almacenada.')
		respuesta = str(listado.page)
	elif request.method == 'PUT':
		try:
			listado = Pages.objects.get(name=pagina)
			respuesta = "Esta url ya ha sido incluida, introduzca otra nueva."
		except Pages.DoesNotExist:
			info = request.body
			p = Pages(name=pagina, page=info)
			p.save()
			respuesta = "La url se ha incluido con exito"	
	return HttpResponse(respuesta)

@csrf_exempt
def pagina(request, indice):
	if request.method == 'PUT':
		respuesta = 'Esta pagina no puede ser almacenada, introduzca una cadena de caracteres valida'
	else:
		try:
			listado = Pages.objects.get(id=int(indice))
		except Pages.DoesNotExist:
			return HttpResponse('Lo sentimos, esta pagina no ha sido almacenada.')
		respuesta = str(listado.page)		
	return HttpResponse(respuesta)

def listado(request):
	paginas = Pages.objects.all()
	respuesta = "<ol>"
	for pagina in paginas:
		respuesta += '<li><a href="/' + str(pagina.id) + '">' + str(pagina.name) + '</a>'
	respuesta += "</ol>"
	return HttpResponse(respuesta)



