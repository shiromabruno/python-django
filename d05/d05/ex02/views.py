from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection


def init(request):
    try:
        cursor = connection.cursor()
        table_exists = connection.introspection.table_names()
        if 'ex02_movies' not in table_exists:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex02_movies(
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb INT PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
                );
            """)
            connection.commit()
            connection.close()
            return HttpResponse("Ok")

        connection.close()
        return HttpResponse("Tabela já criada")

    except Exception as e:
        connection.close()
        return HttpResponse(e)


def populate(request):
    movies_data = [
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

    INSERT_DATA = """
        INSERT INTO {table_name}
        (
            episode_nb,
            title,
            director,
            producer,
            release_date
        )
        VALUES
        (
            %s, %s, %s, %s, %s
        );
        """.format(table_name="ex02_movies")

    cursor = connection.cursor()

    result = []

    for movie in movies_data:
        try:
            cursor.execute(INSERT_DATA, [
                movie['episode_nb'],
                movie['title'],
                movie['director'],
                movie['producer'],
                movie['release_date'],
            ])
            result.append("OK")
            connection.commit()
        except Exception as e:
            connection.rollback()
            result.append(e)

    connection.close()
    return HttpResponse("<br/>".join(str(i) for i in result))


def display(request):
    try:
        cursor = connection.cursor()

        SELECT_TABEL = """
            SELECT * FROM {table_name};
            """.format(table_name="ex02_movies")

        cursor.execute(SELECT_TABEL)

        movies = cursor.fetchall()

        connection.close()

        return render(request, 'ex02/display.html', {"movies": movies})
    except Exception as e:
        print(e)
        return HttpResponse("No data available")
