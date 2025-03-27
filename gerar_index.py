import os

# Função para gerar o conteúdo do index.html
def gerar_conteudo_html(titulo, arquivos, tipo, caminho_retorno=""):
    emoji = "📂" if tipo == "categoria" else "📑"
    
    # Adicionar emojis aos botões
    emoji_buttons = {
        "livros": "📚",
        "aulas": "🎓",
        "artigos": "📝"
    }

    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{titulo}</title>
        <link rel="stylesheet" href="../styles.css">
    </head>
    <body>
        <header>
            <h1>{emoji} {titulo}</h1>
        </header>
        <main>
            <ul>
    """
    
    for arquivo in arquivos:
        if arquivo != "index.html":
            if tipo == "categoria":
                emoji = emoji_buttons.get(arquivo.lower(), "")  # Adiciona o emoji apropriado
                html_content += f'<li><a class="button" href="{arquivo}/index.html">{emoji} {arquivo.capitalize()}</a></li>\n'
            else:
                html_content += f'<li><a href="{arquivo}">{arquivo}</a></li>\n'
    
    html_content += """
            </ul>
        </main>
    """
    
    if caminho_retorno:
        html_content += f"""
        <footer>
            <a href="{caminho_retorno}">Retornar: {caminho_retorno}</a>
        </footer>
        """
    
    html_content += """
    </body>
    </html>
    """
    return html_content


# Diretórios principais
base_dirs = ["livros", "aulas", "artigos"]

# Criar index.html na pasta raiz
index_html_content = f"""
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Repositório de Radiologia</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>📂 Repositório de Radiologia</h1>
    </header>
    <main class="categories">
        <ul>
"""

# Adiciona links para as categorias principais com emojis e botões estilizados
for base_dir in base_dirs:
    if base_dir == "livros":
        emoji = "📚"
    elif base_dir == "aulas":
        emoji = "🎓"
    elif base_dir == "artigos":
        emoji = "📝"
    index_html_content += f'<li><a class="button" href="{base_dir}/index.html">{emoji} {base_dir.capitalize()}</a></li>\n'

index_html_content += """
        </ul>
    </main>
    <footer>
        <p>Repositório de Radiologia - 2025</p>
    </footer>
</body>
</html>
"""

# Salvar o index.html da pasta raiz
with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html_content)

# Criar index.html para cada pasta principal e suas subpastas
for base_dir in base_dirs:
    for especialidade in os.listdir(base_dir):  
        pasta_especialidade = os.path.join(base_dir, especialidade)

        # Verifica se é uma pasta
        if os.path.isdir(pasta_especialidade):
            arquivos = [f for f in os.listdir(pasta_especialidade) if os.path.isfile(os.path.join(pasta_especialidade, f)) and f != "index.md"]

            # Criar o conteúdo para o index.html da subpasta
            index_html_content = gerar_conteudo_html(
                especialidade.capitalize(), 
                sorted(arquivos),
                "subpasta",
                caminho_retorno=f"../{base_dir}/index.html"
            )

            # Criar/atualizar o index.html na subpasta
            with open(os.path.join(pasta_especialidade, "index.html"), "w", encoding="utf-8") as f:
                f.write(index_html_content)

print("Todos os arquivos index.html foram gerados com sucesso! 🎉")