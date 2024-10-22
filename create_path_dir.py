import os

def create_path_dir(path_full_novo_projeto):
    # CASO NÃO EXISTA O DIRETÓRIO CRIA
    if os.path.exists(path_full_novo_projeto) == False:
        os.mkdir(path_full_novo_projeto)
    # ENTRA NO DIRETÓRIO
    os.chdir(path_full_novo_projeto)
    return path_full_novo_projeto