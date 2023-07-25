import subprocess

FOLDER_TST = "/home/nk/tst"
FOLDER_OUT = "/home/nk/out"
FOLDER_folder1 = "/home/nk/folder1"
FOLDER_folder2 = "/home/nk/folder2"

def checkcmdoutput(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    if (text in result.stdout and result.returncode == 0) or text in result.stderr:
        return True
    else:
        return False