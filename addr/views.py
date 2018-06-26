from django.shortcuts import render, get_object_or_404
from .models import Friend

# Create your views here.


def friend_list(request):
    friends = Friend.objects.filter(approved_friend=1)
    return render(request, 'addr/friend_list.html',{'friends': friends})


def friend_detail(request, pk):
    friend = get_object_or_404(Friend, pk=pk)
    return render(request, 'addr/friend_detail.html', {'friend': friend})