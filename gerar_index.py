import os

# Diretórios principais
base_dirs = ["livros", "aulas", "artigos"]

for base_dir in base_dirs:
    for especialidade in os.listdir(base_dir):  
        pasta_especialidade = os.path.join(base_dir, especialidade)

        # Verifica se é uma pasta
        if os.path.isdir(pasta_especialidade):
            arquivos = [f for f in os.listdir(pasta_especialidade) if os.path.isfile(os.path.join(pasta_especialidade, f))]

            # Criar conteúdo do index.md
            index_content = f"# 📂 {especialidade}\n\nAqui estão os arquivos disponíveis nesta categoria:\n\n"
            for arquivo in sorted(arquivos):
                index_content += f"- [{arquivo}]({arquivo})\n"

            index_content += "\n📌 *Clique no nome do arquivo para fazer o download ou visualizar diretamente no navegador.*\n"

            # Criar/atualizar o index.md
            with open(os.path.join(pasta_especialidade, "index.md"), "w", encoding="utf-8") as f:
                f.write(index_content)

print("Arquivos index.md gerados com sucesso! 🎉")
