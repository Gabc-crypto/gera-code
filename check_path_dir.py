import os
from get_path_dir import get_path_dir


def check_path_dir():
    dir_path_obtained = get_path_dir()
    if os.path.exists(dir_path_obtained) == False:
        os.mkdir(dir_path_obtained)
    os.chdir(dir_path_obtained)
    return dir_path_obtained