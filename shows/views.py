from django.shortcuts import render, get_object_or_404
from . import models


def shows_all(request):
    shows = models.TvShow.objects.all()
    return render(request, 'shows_list.html', {'shows': shows})


def shows_detail(request, id):
    show = get_object_or_404(models.TvShow, id=id)
    return render(request, 'shows_detail.html', {'show': show})