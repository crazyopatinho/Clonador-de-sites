Ola, Eu novamente... eu fiz um script básico que cópia conteúdo de sites ele acessa uma URL que o usuário fornece e Depois Abaixa os conteúdos dos sites que são: o HTML/ Todos os arquivos Css/ todos os arquivos javascript/ e todas as imagens.
e todos os arquivos de midia. Ele também organiza os arquivos em pastas separadas(exemplo: Css/, js/, img/, media/.) e salve o arquivo HTML como index.html

## Como o Script funciona?
ele pega a URL que o usuário forneceu após isso ele faz uma requisição HTTP e abaixa o conteúdo HTML do site, ele análise o HTML indentifica os arquivos Css e js imagens e mídias, após isso ele salva tudo em pastas no computador ou no térmux.

## Como Executar?
1: **Instale as Bibliotecas Necessárias**
no térmux ou terminal
```pip install requests beautifulsoup4 lxml```
se estiver jogando térmux e dé erro com o lxml rode:
```pkg install libxml2 libxslt
   pkg install clang python-dev
```
2: ** execute o script**
```python copia_site.py
```
digite e URL do site quando solicitado:
```
Digite a URL do site: https://exemplo.com
```
# Como usar os arquivos abaixados?
os arquivos abaixados estarão salvo nas pastas:

index.html > página principal
Css/ > estilos
js/ > Scripts
img/ > imagens
media/ > vídeos e áudios

**voce pode abrir o ```index.html``` para fins de estudo ou para reconstrução de HTML**.
