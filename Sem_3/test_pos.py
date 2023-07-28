from checkcmdoutput import checkcmdoutput
import yaml

with open('config.yml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
FOLDER_TST = data['FOLDER_TST']
FOLDER_OUT = data['FOLDER_OUT']
FOLDER_folder1 = data['FOLDER_folder1']
FOLDER_folder2 = data['FOLDER_folder2']

def test_step1(get_time, get_config_info, clear_dir, get_dir, make_file):
    #test1
    #a : Add files to archive
    res1 = checkcmdoutput(f"cd {FOLDER_TST}; 7z a {FOLDER_OUT}/arx2", "Everything is Ok")
    res2 = checkcmdoutput(f"ls {FOLDER_OUT}", "arx2.7z")
    assert res1 and res2, "test1 FAIl"
def test_step2(get_time, get_config_info, clear_dir, get_dir, make_file):
    #test2
    #e : Extract files from archive (without using directory names)
    res = []
    res.append(checkcmdoutput(f"cd {FOLDER_TST}; 7z a {FOLDER_OUT}/arx2", "Everything is Ok"))
    res.append(checkcmdoutput(f"cd {FOLDER_OUT}; 7z e arx2.7z -o{FOLDER_folder1} -y", "Everything is Ok"))
    for i in make_file:
        res.append(checkcmdoutput(f"ls {FOLDER_folder1}", i))
    assert all(res), "test1 FAIl"
def test_step3(get_time, get_config_info):
    #test3
    #t : Test integrity of archive
    assert checkcmdoutput(f"cd {FOLDER_OUT}; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"
def test_step4(get_time, get_config_info, get_list):
    #test4
    #d : Delete files from archive
    assert checkcmdoutput(f"cd {FOLDER_OUT}; 7z d arx2.7z {get_list[0]}", "Everything is Ok"), "test4 FAIL"
def test_step5(get_time, get_config_info):
    #test5
    #u : Update files to archive
    assert checkcmdoutput(f"cd {FOLDER_OUT}; 7z u arx2.7z", "Everything is Ok"), "test5 FAIL"
def test_step6(get_time, get_config_info):
    # test6
    #l: List contents of archive
    res1 = checkcmdoutput("cd {}; 7z l arx2.7z".format(FOLDER_OUT, FOLDER_folder1), "arx2.7z")
    res2 = checkcmdoutput("cd {}; 7z l arx2.7z".format(FOLDER_OUT, FOLDER_folder2), "arx2.7z")
    assert res1 and res2, "test1 FAIl"
def test_step7(get_time, get_config_info):
    # test7
    #x : eXtract files with full paths
    res1 = checkcmdoutput("cd {}; 7z x arx2.7z -o{} -y".format(FOLDER_OUT, FOLDER_folder2), "Everything is Ok")
    res2 = checkcmdoutput(f"ls {FOLDER_folder2}", "arx2.7z")
    assert res1 and res2, "test1 FAIl"