import sys, requests, json, dewiki

def main(page: str):
 
    wikipedia_url = "https://en.wikipedia.org/w/api.php"
    wikipedia_params = {
        "action": "parse", # Parses content and returns parser output. https://www.mediawiki.org/wiki/API:Main_module
        "page": query_busca,
        "prop": "wikitext", # Wikitext with HTML tags removed and entities replaced. https://www.mediawiki.org/wiki/API:Properties
        "format": "json",
        "redirects": "true" # Returns all redirects to the given pages. 
    }

    try:
        retorno_wikipedia = requests.get(url=wikipedia_url, params=wikipedia_params)
        # print(retorno_wikipedia) # --> <Response [200]>
    except Exception as e:
        print(f'Erro na chamada da API Wikipedia: {e}. Retorno da API Wikipedia: {retorno_wikipedia}')
        return
    
    try:
        data = json.loads(retorno_wikipedia.text)
        #print(data)
    except Exception as e:
        print(f'Erro no json.loads: {e}. Retorno da API Wikipedia: {retorno_wikipedia}')
        return
    
    if data.get("error") is not None:
        # exemplo de erro pra cair aqui: The page you specified doesn't exist.
        # exemplo do 'data': {'error': {'code': 'missingtitle', 'info': "The page you specified doesn't exist.", '*': 'See https://en.wikipedia.org/w/api.php for API usage. Subscribe to the mediawiki-api-announce mailing list at &lt;https://lists.wikimedia.org/postorius/lists/mediawiki-api-announce.lists.wikimedia.org/&gt; for notice of API deprecations and breaking changes.'}, 'servedby': 'mw1392'}
        print(f'Retorno da API Wikipedia com Erro: {data["error"]["info"]}')
        return

    # Exemplo de Wiki markup text: {Short description|Viennoiserie sweet roll}}
    return (dewiki.from_string(data["parse"]["wikitext"]["*"])) # Retorna sem Wiki markup text


if __name__ == '__main__':

    # pip install -r ./requirement.txt
    # Python module to remove wiki markup text. Whenever you have data that contains wiki markup and want to convert it into human readable plain text, you can use dewiki to do so.
    # Exemplo de Wiki markup text: {Short description|Viennoiserie sweet roll}}

    if len(sys.argv) != 2:
        print("Necessario 2 argumentos apenas: request_wikipedia.py e o string de busca no Wikipedia")
        sys.exit(1)

    query_busca = sys.argv[1]

    retorno_wikipedia = main(query_busca)

    try:
        f = open("{}.wiki".format(sys.argv[1]), "w")
        f.write(retorno_wikipedia)
        f.close
    except Exception as e:
        print(f'Erro na criacao do arquivo .wiki: {e}')