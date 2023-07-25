from checkcmdoutput import checkcmdoutput, FOLDER_OUT, FOLDER_folder1

def test_step1():
    #test1
    assert checkcmdoutput(f"cd {FOLDER_OUT}; 7z e bad.7z -o{FOLDER_folder1} -y", "Can not open the file as [7z] archive"), "test2 FAIL"
def test_step2():
    #test2
    assert checkcmdoutput(f"cd {FOLDER_OUT}; 7z t bad.7z", "Can not open the file as [7z] archive"), "test2 FAIL"