from sshcheckers import ssh_checkout, upload_file, getout
import yaml

with open('config.yml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
FOLDER_TST = data['FOLDER_TST']
FOLDER_OUT = data['FOLDER_OUT']
FOLDER_folder1 = data['FOLDER_folder1']
FOLDER_folder2 = data['FOLDER_folder2']
def save_log(starttime, name):
    with open(name, 'w') as f:
        f.write(getout("journalctl --since '{}'".format(starttime)))

def test_step1(start_time):
    res = []
    upload_file(data["ip"], data["user"], data["passwd"], 'p7zip-full.deb', '/home/user2/p7zip-full.deb')
    res.append(ssh_checkout(data["ip"], data["user"], data["passwd"], 'echo "qwerty28" | sudo -S dpkg -i /home/user2/p7zip-full.deb',
                     'Настраивается пакет'))
    res.append(ssh_checkout(data["ip"], data["user"], data["passwd"], 'echo "qwerty28" | sudo -S dpkg -s p7zip-full',
                            'Status: install ok installed'))
    save_log(start_time, 'log_test1')
    assert all(res), 'test1 FAIL'

def test_step2(start_time, clear_dir, get_dir, make_file):
    #test1
    #a : Add files to archive
    res1 = ssh_checkout(data["ip"], data["user"], data["passwd"], f"cd {FOLDER_TST}; 7z a {FOLDER_OUT}/arx2", "Everything is Ok")
    res2 = ssh_checkout(data["ip"], data["user"], data["passwd"], f"ls {FOLDER_OUT}", "arx2.7z")
    save_log(start_time, 'log_test2')
    assert res1 and res2, "test2 FAIl"

def test_step3(start_time, clear_dir, get_dir, make_file):
    #test2
    #e : Extract files from archive (without using directory names)
    res = []
    res.append(ssh_checkout(data["ip"], data["user"], data["passwd"],f"cd {FOLDER_TST}; 7z a {FOLDER_OUT}/arx2", "Everything is Ok"))
    res.append(ssh_checkout(data["ip"], data["user"], data["passwd"],f"cd {FOLDER_OUT}; 7z e arx2.7z -o{FOLDER_folder1} -y", "Everything is Ok"))
    for i in make_file:
        res.append(ssh_checkout(data["ip"], data["user"], data["passwd"],f"ls {FOLDER_folder1}", i))
    save_log(start_time, 'log_test3')
    assert all(res), "test3 FAIl"

def test_step4(start_time):
    #test3
    #t : Test integrity of archive
    save_log(start_time, 'log_test4')
    assert ssh_checkout(data["ip"], data["user"], data["passwd"],f"cd {FOLDER_OUT}; 7z t arx2.7z", "Everything is Ok"), "test4 FAIL"

def test_step5(start_time):
    #test4
    #d : Delete files from archive
    save_log(start_time, 'log_test5')
    assert ssh_checkout(data["ip"], data["user"], data["passwd"],f"cd {FOLDER_OUT}; 7z d arx2.7z", "Everything is Ok"), "test5 FAIL"

def test_step6(start_time):
    #test5
    #u : Update files to archive
    save_log(start_time, 'log_test6')
    assert ssh_checkout(data["ip"], data["user"], data["passwd"],f"cd {FOLDER_OUT}; 7z u arx2.7z", "Everything is Ok"), "test6 FAIL"

def test_step7(start_time):
    # test6
    #l: List contents of archive
    res1 = ssh_checkout(data["ip"], data["user"], data["passwd"], "cd {}; 7z l arx2.7z".format(FOLDER_OUT, FOLDER_folder1), "arx2.7z")
    res2 = ssh_checkout(data["ip"], data["user"], data["passwd"], "cd {}; 7z l arx2.7z".format(FOLDER_OUT, FOLDER_folder2), "arx2.7z")
    save_log(start_time, 'log_test7')
    assert res1 and res2, "test7 FAIl"

def test_step8(start_time):
    # test7
    #x : eXtract files with full paths
    res1 = ssh_checkout(data["ip"], data["user"], data["passwd"], "cd {}; 7z x arx2.7z -o{} -y".format(FOLDER_OUT, FOLDER_folder2), "Everything is Ok")
    res2 = ssh_checkout(data["ip"], data["user"], data["passwd"], f"ls {FOLDER_folder2}", "arx2.7z")
    save_log(start_time, 'log_test8')
    assert res1 and res2, "test8 FAIl"