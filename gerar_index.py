import os

# Diretórios principais
base_dirs = ["livros", "aulas", "artigos"]

# Criar index.html na pasta raiz
index_html_content = """<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Repositório de Radiologia</title>
</head>
<body>
    <h1>📂 Repositório de Radiologia</h1>
    <ul>
"""

# Adiciona links para as categorias principais
for base_dir in base_dirs:
    index_html_content += f'        <li><a href="{base_dir}/index.html">{base_dir.capitalize()}</a></li>\n'

index_html_content += """    </ul>
</body>
</html>
"""

# Salvar o index.html da pasta raiz
with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html_content)

# Criar index.html para cada pasta principal e suas subpastas
for base_dir in base_dirs:
    # Criar um index.html dentro de cada pasta base
    index_html_content = f"""<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{base_dir.capitalize()}</title>
</head>
<body>
    <h1>📂 {base_dir.capitalize()}</h1>
    <ul>
"""

    subpastas = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]

    for subpasta in sorted(subpastas):
        index_html_content += f'        <li><a href="{subpasta}/index.html">{subpasta}</a></li>\n'

    index_html_content += """    </ul>
</body>
</html>
"""

    with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html_content)

    # Criar index.html para cada subpasta dentro das categorias
    for especialidade in subpastas:
        pasta_especialidade = os.path.join(base_dir, especialidade)

        arquivos = [f for f in os.listdir(pasta_especialidade) if os.path.isfile(os.path.join(pasta_especialidade, f)) and f != "index.md"]

        index_html_content = f"""<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{especialidade}</title>
</head>
<body>
    <h1>📂 {especialidade}</h1>
    <ul>
"""

        for arquivo in sorted(arquivos):
            index_html_content += f'        <li><a href="{arquivo}">{arquivo}</a></li>\n'

        index_html_content += """    </ul>
</body>
</html>
"""

        # Criar/atualizar o index.html na subpasta
        with open(os.path.join(pasta_especialidade, "index.html"), "w", encoding="utf-8") as f:
            f.write(index_html_content)

print("Todos os arquivos index.html foram gerados com sucesso! 🎉")