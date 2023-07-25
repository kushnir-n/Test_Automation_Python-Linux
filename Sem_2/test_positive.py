from checkcmdoutput import checkcmdoutput, FOLDER_TST, FOLDER_OUT, FOLDER_folder1, FOLDER_folder2

def test_step1():
    #test1
    #a : Add files to archive
    res1 = checkcmdoutput(f"cd {FOLDER_TST}; 7z a ../out/arx2", "Everything is Ok")
    res2 = checkcmdoutput(f"ls {FOLDER_OUT}", "arx2.7z")
    assert res1 and res2, "test1 FAIl"
def test_step2():
    #test2
    #e : Extract files from archive (without using directory names)
    res1 = checkcmdoutput(f"cd {FOLDER_OUT}; 7z e arx2.7z -o{FOLDER_folder1} -y", "Everything is Ok")
    res2 = checkcmdoutput(f"ls {FOLDER_folder1}", "test1.txt")
    assert res1 and res2, "test1 FAIl"
def test_step3():
    #test3
    #t : Test integrity of archive
    assert checkcmdoutput(f"cd {FOLDER_OUT}; 7z t arx2.7z", "Everything is Ok"), "test3 FAIL"
def test_step4():
    #test4
    #d : Delete files from archive
    assert checkcmdoutput(f"cd {FOLDER_OUT}; 7z d arx2.7z", "Everything is Ok"), "test4 FAIL"
def test_step5():
    #test5
    #u : Update files to archive
    assert checkcmdoutput(f"cd {FOLDER_OUT}; 7z u arx2.7z", "Everything is Ok"), "test5 FAIL"
def test_step6():
    # test6
    #l: List contents of archive
    res1 = checkcmdoutput("cd {}; 7z l arx2.7z".format(FOLDER_OUT, FOLDER_folder1), "arx2.7z")
    res2 = checkcmdoutput("cd {}; 7z l arx2.7z".format(FOLDER_OUT, FOLDER_folder2), "arx2.7z")
    assert res1 and res2, "test1 FAIl"
def test_step7():
    # test7
    #x : eXtract files with full paths
    res1 = checkcmdoutput("cd {}; 7z x arx2.7z -o{} -y".format(FOLDER_OUT, FOLDER_folder2), "Everything is Ok")
    res2 = checkcmdoutput(f"ls {FOLDER_folder2}", "arx2.7z")
    assert res1 and res2, "test1 FAIl"