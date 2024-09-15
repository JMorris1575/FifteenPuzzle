from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings

from .tools import generate_puzzle

@login_required
def entry_view(request):
    return render(request, 'fifteen/entry.html')

@login_required
def puzzle_view(request):
    if request.GET.get('command') == 'get_puzzle':
        size = int(request.GET.get('size'))
        grid, solution = generate_puzzle(size)
        puzzle_map = {
                      'side_tiles': size,
                      'start_positions': grid,
                      'solution': solution,
                      'style': 'numeric'
                      }
        return JsonResponse(puzzle_map)

    return render(request, 'fifteen/puzzle.html')

@login_required
def clock_view(request):
    return render(request, 'fifteen/clock.html')

@login_required
def game_view(request):
    return render(request, 'fifteen/game.html')
