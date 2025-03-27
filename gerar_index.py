import os

# Função para gerar o conteúdo do index.html
def gerar_conteudo_html(titulo, arquivos, tipo, caminho_retorno_pasta="", caminho_retorno_inicial=""):
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
        <link rel="stylesheet" href="../../styles.css">
    </head>
    <body>
        <header>
            <h1>{emoji} {titulo}</h1>
        </header>
        <main>
            <ul>
    """
    
    for arquivo in arquivos:
        if arquivo != "index.html" and arquivo != ".DS_Store":  # Ignorar arquivos ocultos
            if tipo == "categoria":
                emoji = emoji_buttons.get(arquivo.lower(), "")  # Adiciona o emoji apropriado
                html_content += f'<li><a class="button" href="{arquivo}/index.html">{emoji} {arquivo.capitalize()}</a></li>\n'
            else:
                html_content += f'<li><a class="button" href="{arquivo}">{emoji} {arquivo}</a></li>\n'
    
    html_content += """
            </ul>
        </main>
    """
    
    if caminho_retorno_pasta or caminho_retorno_inicial:
        html_content += "<footer>\n"
        if caminho_retorno_pasta:
            html_content += f'<a class="button return-button" href="{caminho_retorno_pasta}">Retornar à pasta anterior</a><br>\n'
        if caminho_retorno_inicial:
            html_content += f'<a class="button return-button" href="{caminho_retorno_inicial}">Retornar à página inicial</a>\n'
        html_content += "</footer>"
    
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
    emoji = {"livros": "📚", "aulas": "🎓", "artigos": "📝"}.get(base_dir, "")
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
                caminho_retorno_pasta="../index.html",  # Link para a pasta anterior
                caminho_retorno_inicial="../../index.html"  # Link para a página inicial
            )

            # Criar/atualizar o index.html na subpasta
            with open(os.path.join(pasta_especialidade, "index.html"), "w", encoding="utf-8") as f:
                f.write(index_html_content)

# Corrigir botões duplicados nas pastas principais
for base_dir in base_dirs:
    index_path = os.path.join(base_dir, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            content = f.read()
        # Remove qualquer footer existente antes de adicionar o correto
        content = content.split("<footer>")[0]  
        content += """
        <footer>
        <a class="button return-button" href="../index.html">Retornar à página inicial</a>
        </footer>
        </main>
        </body>
        </html>
        """
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(content)

print("Todos os arquivos index.html foram gerados com sucesso! 🎉")