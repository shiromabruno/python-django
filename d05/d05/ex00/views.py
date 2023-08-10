from django.http import HttpResponse
from django.db import connection

# Create your views here.

def init(request):
    try:
        cursor = connection.cursor()
        table_exists = connection.introspection.table_names()
        if 'ex00_movies' not in table_exists:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex00_movies(
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
