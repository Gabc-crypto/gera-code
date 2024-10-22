from check_path_dir import check_path_dir
import bash_commands
from create_path_dir import create_path_dir

# CAMINHO OBTIDO E VERIFICADO
verified_dir_path = check_path_dir()

# SOLICITA AO USUÁRIO UM NOME PARA O PROJETO A SER CRIADO
dir_novo_projeto = input('Digite o nome do Projeto a ser criado: ')

# VARIÁVEL COM O CAMINHO COMPLETO DO PROJETO A SER CRIADO
path_full_novo_projeto = f'{verified_dir_path}/{dir_novo_projeto}'

# CRIA UM CAMINHO COMPLETO PARA O PROJETO CASO NÃO EXISTA
path_created_dir = create_path_dir(path_full_novo_projeto)

bash_commands.update()
bash_commands.install_pip()
bash_commands.implementation_venv()
bash_commands.open_vscode(path_created_dir)