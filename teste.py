from classes.relatorio import RelatorioExcel

rel = RelatorioExcel("Dobra")
rel.carregar_dados()
rel.carregar_modelo()

if rel.wb:
    rel.preencher_planilha()
    rel.salvar_relatorio()
else:
    print("Erro: não foi possível carregar o modelo.")