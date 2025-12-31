import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import re

# URL do site
url = input("Digite a URL do site: ").strip()
if not url.startswith(("http://", "https://")):
    url = "https://" + url

# Faz a requisição
response = requests.get(url)
html = response.text

# Salva o HTML
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

# Usa BeautifulSoup com lxml
soup = BeautifulSoup(html, "lxml")

# Cria pastas
os.makedirs("css", exist_ok=True)
os.makedirs("js", exist_ok=True)
os.makedirs("img", exist_ok=True)
os.makedirs("media", exist_ok=True)

# Função para limpar nomes de arquivos inválidos
def limpar_nome(nome):
    return re.sub(r'[^\w\-.]', '_', nome)

# Baixa arquivos CSS
for css in soup.find_all("link", rel="stylesheet"):
    href = css.get("href")
    if href:
        file_url = urljoin(url, href)
        file_name = limpar_nome(os.path.basename(href))
        r = requests.get(file_url)
        with open(os.path.join("css", file_name), "wb") as f:
            f.write(r.content)

# Baixa arquivos JS
for js in soup.find_all("script", src=True):
    src = js.get("src")
    if src:
        file_url = urljoin(url, src)
        file_name = limpar_nome(os.path.basename(src))
        r = requests.get(file_url)
        with open(os.path.join("js", file_name), "wb") as f:
            f.write(r.content)

# Baixa imagens
for img in soup.find_all("img"):
    src = img.get("src")
    if src:
        file_url = urljoin(url, src)
        file_name = limpar_nome(os.path.basename(src))
        try:
            r = requests.get(file_url)
            with open(os.path.join("img", file_name), "wb") as f:
                f.write(r.content)
        except Exception as e:
            print(f"Erro ao baixar {file_url}: {e}")

# Baixa arquivos de mídia (vídeos, áudio)
for media in soup.find_all(["video", "audio", "source"]):
    src = media.get("src")
    if src:
        file_url = urljoin(url, src)
        file_name = limpar_nome(os.path.basename(src))
        try:
            r = requests.get(file_url)
            with open(os.path.join("media", file_name), "wb") as f:
                f.write(r.content)
        except Exception as e:
            print(f"Erro ao baixar {file_url}: {e}")

print("Download concluído! HTML, CSS, JS, imagens e mídia salvos.")
