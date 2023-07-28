from checkcmdoutput import checkcmdoutput
import yaml

with open('config.yml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
FOLDER_TST = data['FOLDER_TST']
FOLDER_OUT = data['FOLDER_OUT']
FOLDER_folder1 = data['FOLDER_folder1']
FOLDER_folder2 = data['FOLDER_folder2']

def test_step1(get_time, get_config_info, get_bad):
    #test1
    assert checkcmdoutput(f"cd {FOLDER_OUT}; 7z e bad.7z -o{FOLDER_folder1} -y", "Can not open the file as [7z] archive"), "test2 FAIL"
def test_step2(get_time, get_config_info, get_bad):
    #test2
    assert checkcmdoutput(f"cd {FOLDER_OUT}; 7z t bad.7z", "Can not open the file as [7z] archive"), "test2 FAIL"