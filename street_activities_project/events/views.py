from django.http import HttpResponse


def events_list(request):
    return HttpResponse("Список событий")


def events_detail(request, pk):
    return HttpResponse(f"Событие номер {pk}")
