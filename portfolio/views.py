from django.shortcuts import render, get_object_or_404
from .models import CardProject


def all_cards(request):
    cards = CardProject.objects.order_by('-date', '-time')
    return render(request, 'portfolio/all_cards.html', {'cards': cards})


def detail(request, card_id):
    card = get_object_or_404(CardProject, pk=card_id)
    return render(request, 'portfolio/detail.html', {'card': card})

