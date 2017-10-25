from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .models import Board

# Create your views here.

def home(request):
    #return HttpResponse('Hello, World!')
    boards = Board.objects.all()
    #boards_names = list()
    return render(request, 'home.html', {'boards': boards})
    for board in boards:
        boards_names.append(board.name)
    response_html = '<br>'.join(boards_names)
    return HttpResponse(response_html)

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    # try:
    #     board = Board.objects.get(pk=pk)
    # except Board.DoesNotExist:
    #     raise Http404
    return render(request, 'topics.html', {'board': board})


