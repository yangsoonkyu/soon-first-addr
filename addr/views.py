from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Friend
from .forms import FriendForm

# Create your views here.


def friend_list(request):
    friends = Friend.objects.filter(approved_friend=1)
    return render(request, 'addr/friend_list.html',{'friends': friends})


def friend_detail(request, pk):
    friend = get_object_or_404(Friend, pk=pk)
    return render(request, 'addr/friend_detail.html', {'friend': friend})


def friend_new(request):
    if request.method == "POST":
        form = FriendForm(request.POST)
        if form.is_valid():
            friend = form.save(commit=False)
            friend.author = User.objects.get(username='admin')
            # friend.author = request.user
            friend.save()
            return redirect('addr:friend_detail', pk=friend.pk)
    else:
        form = FriendForm()
    return render(request, 'addr/friend_edit.html', {'form': form})


def friend_edit(request, pk):
    friend = get_object_or_404(Friend, pk=pk)
    if request.method == "POST":
        form = FriendForm(request.POST, instance=friend)
        if form.is_valid():
            friend = form.save(commit=False)
            friend.author = User.objects.get(username='admin')
            # friend.author = request.user
            friend.save()
            return redirect('addr:friend_detail', pk=friend.pk)
    else:
        form = FriendForm(instance=friend)
    return render(request, 'addr/friend_edit.html', {'form': form})