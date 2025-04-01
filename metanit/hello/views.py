from django.http import HttpResponse
   
def index(request):
    return HttpResponse("<h2>Главная</h2>")
  
def user(request):
    age = request.GET.get("age", 0)
    name = request.GET.get("name", "Undefined")
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")