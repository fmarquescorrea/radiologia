import os

def gerar_lista_arquivos(caminho_subpasta):
    """Gera um fragmento HTML com a lista de arquivos da subpasta, excluindo indesejados."""
    arquivos = [
        f'<li><a class="file-link" href="{arquivo}">{arquivo}</a></li>'  # Adicionamos a classe file-link
        for arquivo in sorted(os.listdir(caminho_subpasta))
        if os.path.isfile(os.path.join(caminho_subpasta, arquivo))  
        and not arquivo.startswith("template_")  
        and not arquivo.startswith(".")  
        and arquivo != "arquivos.html"
    ]
    return "\n".join(arquivos)

def gerar_fragmento_arquivos(caminho_base):
    """Percorre todas as subpastas e cria um fragmento de lista de arquivos."""
    for pasta_raiz in ["aulas", "artigos", "livros"]:
        caminho_pasta_raiz = os.path.join(caminho_base, pasta_raiz)
        if not os.path.isdir(caminho_pasta_raiz):
            continue
        
        # Aqui, estamos agora iterando pelas subpastas dentro de cada pasta principal
        for subpasta in os.listdir(caminho_pasta_raiz):
            caminho_subpasta = os.path.join(caminho_pasta_raiz, subpasta)
            if os.path.isdir(caminho_subpasta):  # Somente subpastas são consideradas
                fragmento_html = gerar_lista_arquivos(caminho_subpasta)
                caminho_arquivos_html = os.path.join(caminho_subpasta, "arquivos.html")
                with open(caminho_arquivos_html, "w", encoding="utf-8") as f:
                    f.write(fragmento_html)

if __name__ == "__main__":
    caminho_atual = os.path.dirname(os.path.abspath(__file__))
    gerar_fragmento_arquivos(caminho_atual)