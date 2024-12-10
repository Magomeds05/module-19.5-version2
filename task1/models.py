from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()

class CreatePost(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=1000, decimal_places=2)
    description = models.TextField(max_length=300)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')



#python manage.py shell
#from task1.models import Buyer
#Post.objects.all()
#Buyer.objects.create(name= 'Magomed', balance= '5000', age= '22')
#Buyer.objects.create(name= 'Denis', balance= '7500', age= '30')
#Buyer.objects.create(name= 'Mark', balance= '300', age= '15')
#from task1.models import Game
#Game.objects.create(title= 'Batman Origin', cost = '100', size = '13.5', description = 'Game about a Batman', age_limited = '1')
#Game.objects.create(title= 'Dota 2', cost = '300', size = '34', description = 'Worst game ever', age_limited = '0')
#Game.objects.create(title= 'Fallout 4', cost = '500', size = '40', description = 'My fw game', age_limited = '1')
#from task1.models import *
#first_buyer = Buyer.objects.get(name= 'Magomed')
#second_buyer = Buyer.objects.get(name= 'Denis')
#Game.objects.get(id=1).buyer.set((first_buyer, second_buyer))
#Game.objects.get(id=2).buyer.set((first_buyer, second_buyer))
#third_buyer = Buyer.objects.get(name= 'Mark')
#Game.objects.get(id=2).buyer.set((first_buyer, third_buyer))
#Game.objects.get(id=3).buyer.set((first_buyer, third_buyer))

#python manage.py startapp postapp
#python manage.py
#python manage.py runserver
#python manage.py createsuperuser
#python manage.py
#Post.objects.filter(created_at = '2024-12-06 12:17:05.916308')