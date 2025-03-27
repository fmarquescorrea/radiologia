import os

# Diretórios principais
base_dirs = ["livros", "aulas", "artigos"]

# Código CSS para o estilo
css_content = """
/* Reset básico */
body {
    font-family: Arial, sans-serif;
    text-align: center;
    margin: 0;
    padding: 0;
    background-color: #f8f8f8;
}

/* Cabeçalho */
header {
    background-color: #004080;
    color: white;
    padding: 20px;
}

/* Seção principal */
.categories {
    margin-top: 50px;
}

/* Botões estilizados */
.button {
    display: inline-block;
    margin: 10px;
    padding: 15px 30px;
    background-color: #007BFF;
    color: white;
    text-decoration: none;
    font-size: 18px;
    border-radius: 8px;
    transition: 0.3s;
}

.button:hover {
    background-color: #0056b3;
}

/* Rodapé */
footer {
    margin-top: 50px;
    font-size: 14px;
    color: #333;
}
"""

# Criar index.html na pasta raiz
index_html_content = f"""
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Repositório de Radiologia</title>
    <style>
    {css_content}
    </style>
</head>
<body>
    <header>
        <h1>📂 Repositório de Radiologia</h1>
    </header>
    <div class="categories">
        <ul>
"""

# Adiciona links para as categorias principais
for base_dir in base_dirs:
    index_html_content += f'<li><a class="button" href="{base_dir}/index.html">{base_dir.capitalize()}</a></li>\n'

index_html_content += """
        </ul>
    </div>
    <footer>
        <p>© 2025 Repositório de Radiologia</p>
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

            # Criar index.html para cada subpasta
            index_html_content = f"""
            <!DOCTYPE html>
            <html lang="pt">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{especialidade}</title>
                <style>
                {css_content}
                </style>
            </head>
            <body>
                <header>
                    <h1>📂 {especialidade}</h1>
                </header>
                <div class="categories">
                    <ul>
            """

            for arquivo in sorted(arquivos):
                index_html_content += f'<li><a class="button" href="{arquivo}">{arquivo}</a></li>\n'

            index_html_content += """
                    </ul>
                </div>
                <footer>
                    <p>© 2025 Repositório de Radiologia</p>
                </footer>
            </body>
            </html>
            """

            # Criar/atualizar o index.html na subpasta
            with open(os.path.join(pasta_especialidade, "index.html"), "w", encoding="utf-8") as f:
                f.write(index_html_content)

print("Todos os arquivos index.html foram gerados com sucesso! 🎉")