from django.shortcuts import render
from .models import Friend

# Create your views here.


def friend_list(request):
    friends = Friend.objects.filter(approved_friend=1)
    return render(request, 'addr/friend_list.html',{'friends': friends})