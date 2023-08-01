import random
import string
import pytest
import yaml
from sshcheckers import ssh_checkout
from datetime import datetime

with open('config.yml', 'r') as f:
    data = yaml.safe_load(f)
FOLDER_TST = data['FOLDER_TST']
FOLDER_OUT = data['FOLDER_OUT']
FOLDER_folder1 = data['FOLDER_folder1']
FOLDER_folder2 = data['FOLDER_folder2']

@pytest.fixture()
def get_dir():
    return ssh_checkout(data["ip"], data["user"], data["passwd"],f'mkdir {FOLDER_OUT} {FOLDER_TST} {FOLDER_folder1} {FOLDER_folder2}')

@pytest.fixture()
def make_file():
    list_files = []
    for i in range(data['count']):
        file_name = ''.join(random.choices(string.ascii_letters+string.digits, k=5))
        if ssh_checkout(data["ip"], data["user"], data["passwd"],f'cd {FOLDER_TST}; dd if=/dev/urandom of={file_name} bs={data["size"]} count={data["count"]} iflag=fullblock'):
            list_files.append(file_name)
    return list_files

@pytest.fixture()
def clear_dir():
    return ssh_checkout(data["ip"], data["user"], data["passwd"],f'rm -rf {FOLDER_OUT} {FOLDER_TST} {FOLDER_folder1} {FOLDER_folder2}')

@pytest.fixture()
def start_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
