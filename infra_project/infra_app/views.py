from django.http import HttpResponse


def index(request):
    return HttpResponse(
        '<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ?autoplay=1">На вторую страницу</a>'
    )


def second_page(request):
    return HttpResponse('А это вторая страница')
