import os
choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 Anubis.py')
    run('mkdir /usr/share/Anubis')
    run('cp Anubis.py /usr/share/Anubis/Anubis.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/Anubis/Anubis.py "$@"')
    with open('/usr/bin/Anubis','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/Anubis & chmod +x /usr/share/Anubis/Anubis.py')
    print('''\n\done install Anubis ip changer \nfrom now just type \x1b[6;30;42mdbc\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/Anubis ')
    run('rm /usr/bin/Anubis ')
    print('[!] Done install IP Changer Anubis')
