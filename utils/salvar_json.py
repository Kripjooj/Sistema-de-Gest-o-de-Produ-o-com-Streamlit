import os
import json

def salvar_producao(producao):
    pasta = "database"
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    caminho_arquivo = os.path.join(pasta, "producao.json")

    # Se o arquivo já existe e não está vazio, carrega os dados
    if os.path.exists(caminho_arquivo) and os.path.getsize(caminho_arquivo) > 0:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
    else:
        dados = []

    # Adiciona a nova produção ao final da lista
    dados.append(producao.to_dict())

    # Salva de volta no arquivo
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)