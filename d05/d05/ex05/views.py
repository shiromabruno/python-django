from django.shortcuts import redirect, render
from .models import Movies
from django import db
from django.http import HttpResponse
# Create your views here.


def populate(request):
    data = [
        {
            "episode_nb": 1,
            "title": "The Phantom Menace",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "1999-05-19"
        },
        {
            "episode_nb": 2,
            "title": "Attack of the Clones",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2002-05-16"
        },
        {
            "episode_nb": 3,
            "title": "Revenge of the Sith",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2005-05-19"
        },
        {
            "episode_nb": 4,
            "title": "A New Hope",
            "director": "George Lucas",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "1977-05-25"
        },
        {
            "episode_nb": 5,
            "title": "The Empire Strikes Back",
            "director": "Irvin Kershner",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "1980-05-17"
        },
        {
            "episode_nb": 6,
            "title": "Return of the Jedi",
            "director": "Richard Marquand",
            "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
            "release_date": "1983-05-25"
        },
        {
            "episode_nb": 7,
            "title": "The Force Awakens",
            "director": "J. J. Abrams",
            "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
            "release_date": "2015-12-11"
        }
    ]

    result = []
    for value in data:
        try:
            Movies.objects.create(
                episode_nb=value['episode_nb'],
                title=value['title'],
                director=value['director'],
                producer=value['producer'],
                release_date=value['release_date'],
            )
            result.append("OK")
        except db.Error as e:
            result.append(e)

    return HttpResponse("<br/>".join(str(i) for i in result))

def display(request):
    try:
        movies = Movies.objects.all()
        if len(movies) == 0:
            raise Movies.DoesNotExist
        
        return render(request, 'ex05/display.html', {"movies": movies})
    except Exception as e:
        print(e)
        return HttpResponse("No data available")
    
def remove(request):
    try:
        if request.method == 'POST':
            teste = Movies.objects.filter(episode_nb=request.POST['episode_nb']).delete()
            print(teste)

            return redirect('remove-orm')
        else:
            movies = Movies.objects.all()
            if len(movies) == 0:
                raise Movies.DoesNotExist
            return render(request, 'ex05/remove.html', {"movies": movies})
    except Exception as e:
        print(e)
        return HttpResponse("No data available")

