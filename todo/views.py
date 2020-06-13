from django.shortcuts import render
from .models import Item
# Create your views here.

# render the item, define the context vocabular, then add as a return element 
def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html',context)
