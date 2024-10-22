from pathlib import Path
import os

def get_path_dir(folder:str = 'new_project'):
    diretorio_home = Path.home()
    os.chdir(diretorio_home)
    return  f'{diretorio_home}/{folder}'