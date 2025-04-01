from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Главная</h2>")
  
def user(request, name="Undefined", age =0):
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")

def about(request, name, age):
    return HttpResponse(f"""
            <h2>О пользователе</h2>
            <p>Имя: {name}</p>
            <p>Возраст: {age}</p>
    """)
 
def contact(request):
    return HttpResponse("<h2>Контакты</h2>")