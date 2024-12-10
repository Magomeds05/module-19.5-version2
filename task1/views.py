from django.shortcuts import render
from django.http import HttpResponse
from .models import Buyer, Game


def main_page(request):
    return render(request, 'platform.html')

def games(request):

    games = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 2"]}
    return render(request, 'games.html', context=games)

def cart(request):
    return render(request, 'cart.html')

def menu(request):
    return render(request, 'menu.html')

def sign_up_by_html(request):
    Buyers = Buyer.objects.all()  #Вместо списка псевдо-пользователей получайте записи из таблицы Buyer.
    info = {}
    context = {'info': info,}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        for buyer in Buyers:  #Измените условие регистрации так, чтобы пользователь добавлялся только в том случае, если его нет в коллекции Buyer.
            if username == buyer.name:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'registration_page.html', context)

        if password == repeat_password and int(age) >= 18:
            Buyer.objects.create(name=username, balance=10000, age=age)
            return HttpResponse(f'Приветсвуем, {username}')
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
    return render(request, 'registration_page.html', context)

# Create your views here.
