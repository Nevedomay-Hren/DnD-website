from django.shortcuts import render


# Create your views here.
def dm_index(request):
    return render(request, 'dm/dm_index.html')


def players_index(request):
    return render(request, 'dm/players_index.html')


def admin(request):
    return render(request, 'dm/admin.html')


def clear_card(request):
    return render(request, 'dm/clear_card.html')


def my_card(request):
    return render(request, 'dm/my_card.html')


def groups(request):
    return render(request, 'dm/groups.html')
