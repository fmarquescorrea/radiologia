import os

# Diretórios principais
base_dirs = ["livros", "aulas", "artigos"]

# HTML base para as páginas de índice
html_template = """<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titulo}</title>
    <link rel="stylesheet" href="../../style.css">
</head>
<body>
    <header>
        <h1>{titulo}</h1>
        <p>Arquivos disponíveis nesta categoria:</p>
    </header>
    <main>
        <ul class="file-list">
            {lista_arquivos}
        </ul>
        <a href="../../index.html" class="button">🔙 Voltar à Página Inicial</a>
    </main>
    <footer>
        <p>📌 Clique no nome do arquivo para baixar ou visualizar.</p>
    </footer>
</body>
</html>
"""

for base_dir in base_dirs:
    for especialidade in os.listdir(base_dir):  
        pasta_especialidade = os.path.join(base_dir, especialidade)

        # Verifica se é uma pasta
        if os.path.isdir(pasta_especialidade):
            arquivos = sorted(
                [f for f in os.listdir(pasta_especialidade) if not f.startswith(".") and f != "index.html"]
            )

            # Gerar lista em HTML
            lista_arquivos_html = "\n".join(
                [f'<li><a href="{arquivo}">{arquivo}</a></li>' for arquivo in arquivos]
            )

            # Criar conteúdo do index.html
            html_content = html_template.format(
                titulo=f"📂 {especialidade.capitalize()}",
                lista_arquivos=lista_arquivos_html or "<p>🚧 Nenhum arquivo encontrado.</p>"
            )

            # Criar/atualizar index.html
            with open(os.path.join(pasta_especialidade, "index.html"), "w", encoding="utf-8") as f:
                f.write(html_content)

print("Arquivos index.html gerados com sucesso! 🎉")
