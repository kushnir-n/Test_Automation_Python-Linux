from sshcheckers import ssh_checkout, upload_file
def deploy():
    res = []
    upload_file('0.0.0.0', 'user2', 'qwerty28', 'p7zip-full.deb', '/home/user2/p7zip-full.deb')
    res.append(ssh_checkout('0.0.0.0', 'user2', 'qwerty28', 'echo "qwerty28" | sudo -S dpkg -i /home/user2/p7zip-full.deb',
                            'Настраивается пакет'))
    res.append(ssh_checkout('0.0.0.0', 'user2', 'qwerty28', 'echo "qwerty28" | sudo -S dpkg -s p7zip-full',
                            'Status: install ok installed'))
    return res

print(deploy())