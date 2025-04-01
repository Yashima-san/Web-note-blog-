from django.http import HttpResponse
 
def index(request):
    return HttpResponse("Главная страница")
 
def products(request, id):
    return HttpResponse(f"Товар {id}")
 
def comments(request, id):
    return HttpResponse(f"Комментарии о товаре {id}")
 
def questions(request, id):
    return HttpResponse(f"Вопросы о товаре {id}")