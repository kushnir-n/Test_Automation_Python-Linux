import random
import string
import pytest
import yaml
from checkcmdoutput import checkcmdoutput, getout
from datetime import datetime

with open('config.yml', 'r') as f:
    data = yaml.safe_load(f)
FOLDER_TST = data['FOLDER_TST']
FOLDER_OUT = data['FOLDER_OUT']
FOLDER_folder1 = data['FOLDER_folder1']
FOLDER_folder2 = data['FOLDER_folder2']
@pytest.fixture()
def get_dir():
    return checkcmdoutput(f'mkdir{FOLDER_TST} {FOLDER_OUT} {FOLDER_folder1} {FOLDER_folder2}')
@pytest.fixture()
def make_file():
    list_files = []
    for i in range(data['count']):
        file_name = ''.join(random.choices(string.ascii_letters+string.digits, k=5))
        if checkcmdoutput(f'cd {FOLDER_TST}; dd if=/dev/urandom of={file_name} bs={data["size"]} count={data["count"]} iflag=fullblock'):
            list_files.append(file_name)
    return list_files
@pytest.fixture()
def clear_dir():
    return checkcmdoutput(f'rm -f {FOLDER_OUT} {FOLDER_TST} {FOLDER_folder1} {FOLDER_folder2}')
@pytest.fixture()
def get_list():
    return getout(f'ls {FOLDER_TST}')[0]
@pytest.fixture()
def get_bad():
    checkcmdoutput(f"cd {FOLDER_TST}; 7z a {FOLDER_OUT}/bad", "Everything is Ok")
    checkcmdoutput(f"truncate -s 1 {FOLDER_OUT}/bad.7z")
    yield 'bad'
    checkcmdoutput((f'rm -rf {FOLDER_OUT}/bad'))
@pytest.fixture(autouse=True)
def get_time():
    print("Start: {}".format(datetime.now().strftime("%H:%M:%S.%f")))
    yield
    print("Finish: {}".format(datetime.now().strftime("%H:%M:%S.%f")))
@pytest.fixture(autouse=True)
def get_config_info():
    yield
    config_info = getout("cat /proc/loadavg")
    checkcmdoutput("echo 'time: {} count:{} size: {} load: {}'>> stat.txt".format(datetime.now().strftime("%H:%M:%S.%f"), data["count"], data["size"], config_info))