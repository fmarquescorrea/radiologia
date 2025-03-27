import os

# Função para gerar o conteúdo de arquivos.html nas subpastas
def gerar_conteudo_html(arquivos, tipo, pasta_atual):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Arquivos - {pasta_atual.capitalize()}</title>
        <link rel="stylesheet" href="../../styles.css">  <!-- Ajuste para o caminho do CSS -->
    </head>
    <body>
        <header>
            <h1>📂 Arquivos de {pasta_atual.capitalize()}</h1>
        </header>
        <main>
            <ul>
    """

    # Filtrando arquivos que não devem ser listados (como arquivos de código, sistema ou templates)
    arquivos_validos = [f for f in arquivos if f not in ["arquivos.html", "template_subpasta.html", ".DS_Store"]]

    # Adicionar cada arquivo válido à lista
    for arquivo in arquivos_validos:
        html_content += f'<li><a class="button" href="{arquivo}">{arquivo}</a></li>\n'

    html_content += """
            </ul>
        </main>
        <footer>
            <a class="button return-button" href="../template_subpasta.html">Retornar à pasta anterior</a>
            <a class="button return-button" href="../../index.html">Retornar à página inicial</a>
        </footer>
    </body>
    </html>
    """
    return html_content


# Função para gerar os arquivos de cada subpasta
def gerar_arquivos():
    # Diretórios principais
    base_dirs = ["livros", "aulas", "artigos"]

    # Gerar arquivos.html para cada subpasta
    for base_dir in base_dirs:
        for especialidade in os.listdir(base_dir):
            pasta_especialidade = os.path.join(base_dir, especialidade)

            # Verifica se é uma pasta
            if os.path.isdir(pasta_especialidade):
                arquivos = [f for f in os.listdir(pasta_especialidade) if os.path.isfile(os.path.join(pasta_especialidade, f))]

                # Gerar conteúdo do arquivos.html
                arquivos_html_content = gerar_conteudo_html(
                    sorted(arquivos),
                    "subpasta",
                    especialidade
                )

                # Salvar o arquivos.html na subpasta
                with open(os.path.join(pasta_especialidade, "arquivos.html"), "w", encoding="utf-8") as f:
                    f.write(arquivos_html_content)

    print("Arquivos de subpastas gerados com sucesso!")

# Chama a função para gerar os arquivos
gerar_arquivos()