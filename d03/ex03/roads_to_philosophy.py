import sys, requests
from bs4 import BeautifulSoup

class roads_to_philosophy:
    def __init__(self):
        self.link_anterior = []

    def search_wikipeadia(self, query_busca: str): # /wiki/ + query_busca

        URL = 'https://en.wikipedia.org{page}'.format(page=query_busca) # example: https://pt.wikipedia.org/wiki/Python

        try:
            retorno_wiki = requests.get(url=URL)
            retorno_wiki.raise_for_status()
        except Exception as e:
            if (retorno_wiki.status_code == 404):
                return print("It's a dead end !")
            return print(e)

        soup = BeautifulSoup(retorno_wiki.text, 'html.parser') # example: <a class="vector-toc-link" href="#Name"><div class="vector-toc-text"><span class="vector-toc-numb">1</span>Name</div>... etc
        title = soup.find(id='firstHeading').text # example: <h1 class="firstHeading mw-first-heading" id="firstHeading"><span class="mw-page-title-main">Pain au chocolat</span></h1>

        if title in self.link_anterior: # example do Chocolatine: Pain au chocolat, Canada, North America...
            return print("It leads to an infinite loop !")
        
        print(title) # example do Chocolatine: Pain au chocolat, Canada, North America...
        self.link_anterior.append(title) # adiciona os titles acima...

        if title == 'Philosophy':
            return print("{} roads from {} to Philosophy".format(len(self.link_anterior), self.link_anterior[0] if len(self.link_anterior) > 0 else 'Philosophy')) 
        
        content = soup.find(id='mw-content-text') # example: <div class="mw-body-content mw-content-ltr" dir="ltr" id="mw-content-text" lang="en"><div class="mw-parser-output"><div class="shortdescription nomobile noexcerpt noprint searchaux" style="display:none">Viennoiserie sweet roll</div>
        allLinks = content.select('p > a') # <a href="/wiki/Canada" title="Canada">Canada</a>, <a href="/wiki/Belgium" title="Belgium">Belgium</a>... etc

        for link in allLinks: # link = <a href="/wiki/Canada" title="Canada">Canada</a>
            # link.get('href') = /wiki/Canada
            if link.get('href') is not None and link['href'].startswith('/wiki/')\
                    and not link['href'].startswith('/wiki/Wikipedia:') and not link['href'].startswith('/wiki/Help:'):
                return self.search_wikipeadia(link['href']) # /wiki/Canada
        
        return print("It leads to a dead end !.")

def main():

    wiki = roads_to_philosophy() # cria uma instancia com uma lista 'link_anterior' com as buscas anteiores (usado no loop)

    if (len(sys.argv) == 2):
        wiki.search_wikipeadia('/wiki/'+sys.argv[1]) # example: https://pt.wikipedia.org/wiki/Python
    else:
        print("Necessario 2 argumentos apenas: roads_to_philosophy.py e o string de busca no Wikipedia")


if __name__ == '__main__':
    
    # pip install -r ./requirement.txt

    main()