#Esta linha é conhecida como "shebang" e indica qual interpretador deve ser usado para executar o script. Neste caso, estamos usando /bin/sh, que é um interpretador padrão de shell.
#!/bin/sh

#curl -sI "$1": O comando "curl" é usado para fazer uma requisição HTTP para o link bit.ly passado como o primeiro argumento para o script ($1). A opção -s faz o curl ser executado em modo silencioso, sem exibir informações de progresso. A opção -I diz ao curl para fazer uma solicitação HEAD, que retornará apenas os cabeçalhos da resposta HTTP, não o corpo da página.
#grep -i "location:": O comando "grep" é usado para filtrar as linhas de saída do curl e encontrar aquela que contém a palavra "Location:". A opção -i torna a pesquisa case-insensitive, para que não importe se a palavra está em maiúsculas ou minúsculas.
#cut -d' ' -f2: O comando "cut" é usado para extrair a segunda coluna de texto da saída do comando anterior, utilizando o espaço como delimitador. Neste caso, a segunda coluna contém a URL de redirecionamento que desejamos obter.          
curl -sI $1 | grep -i "location: " | cut -d" " -f2


#mobile https://github.com/MarkThisHat/dart_mobile