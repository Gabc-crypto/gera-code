import os
from create_path_dir import create_path_dir

def create_file():
    path_created_dir = create_path_dir(path_created_dir)
    # VERIFICA SE NA RAIZ DO PROJETO EXISTE UM ARQUIVO MAIN
    # CASO NÃO ELE É CRIADO
    if os.path.isfile(f'{path_created_dir}/main.py') == False:
        os.mknod('main.py')

    # EXIBE O CAMINHO COMPLETO DO NOVO PROJETO CRIADO
    print(f'{path_created_dir}/main.py')