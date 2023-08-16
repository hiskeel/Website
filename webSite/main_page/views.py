from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

products =[
    {'name' : 'Prost',
     'price': '210',
     'picture': 'Picture Place'
     },

     {'name' : 'glanec',
     'price': '240',
     'picture': 'Picture Place1'
     }
]


def main_page(request):
    context ={
        'products': products
    }
    return render(request, 'main\main.html', context)

def contuct(request):
    return render(request, 'main\contact.html')