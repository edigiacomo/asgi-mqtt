from django.shortcuts import render


def index(request):
    return render(request, 'print_ws/index.html')
