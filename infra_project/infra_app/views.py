from django.http import HttpResponse


def index(request):
    return HttpResponse('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


def second_page(request):
    return HttpResponse('А это вторая страница')
