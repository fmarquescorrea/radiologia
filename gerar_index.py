import os

# Diretórios principais
base_dirs = ["livros", "aulas", "artigos"]

for base_dir in base_dirs:
    for especialidade in os.listdir(base_dir):  
        pasta_especialidade = os.path.join(base_dir, especialidade)

        # Verifica se é uma pasta
        if os.path.isdir(pasta_especialidade):
            arquivos = [f for f in os.listdir(pasta_especialidade) if os.path.isfile(os.path.join(pasta_especialidade, f))]

            # Criar conteúdo do index.html (em vez de index.md)
            index_content = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{especialidade}</title>
</head>
<body>
    <h1>📂 {especialidade}</h1>
    <p>Aqui estão os arquivos disponíveis nesta categoria:</p>
    <ul>
"""

            for arquivo in sorted(arquivos):
                # Criar links apenas para arquivos, ignorando .index.md
                if not arquivo.startswith('.') and arquivo != 'index.md':
                    index_content += f'        <li><a href="{especialidade}/{arquivo}">{arquivo}</a></li>\n'

            index_content += """
    </ul>
    <p>📌 *Clique no nome do arquivo para fazer o download ou visualizar diretamente no navegador.*</p>
</body>
</html>
"""

            # Criar/atualizar o index.html
            index_html_path = os.path.join(pasta_especialidade, "index.html")
            with open(index_html_path, "w") as f:
                f.write(index_content)

print("Arquivos index.html gerados com sucesso! 🎉")
