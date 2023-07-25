#Задание 1.
#Условие:
#Написать функцию на Python, которой передаются в качестве параметров команда и текст.
#Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и False в противном случае.
##Передаваться должна только одна строка, разбиение вывода использовать не нужно.

import subprocess

def checkcmdoutput(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False

command = 'cat /etc/os-release'
txt = 'PRETTY_NAME="Ubuntu 22.04.1 LTS"\nNAME="Ubuntu"\nVERSION_ID="22.04"\nVERSION="22.04.1 LTS (Jammy Jellyfish)"\nVERSION_CODENAME=jammy\nID=ubuntu\nID_LIKE=debian\nHOME_URL="https://www.ubuntu.com/"\nSUPPORT_URL="https://help.ubuntu.com/"\nBUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"\nPRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"\nUBUNTU_CODENAME=jammy'

print(checkcmdoutput(command, txt))