import os
choice = input('[+] to install press (Y) to uninstall press (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 Erorr.py')
    run('mkdir /usr/share/Erorr')
    run('cp Erorr.py /usr/share/Erorr/Erorr.py')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/Erorr/Erorr.py "$@"')
    with open('/usr/bin/Erorr','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/Erorr & chmod +x /usr/share/Erorr/Erorr.py')
    print('''\n\done install Anubis ip changer \nfrom now just type \x1b[6;30;42mdbc\x1b[0m in terminal ''')
if str(choice)=='N' or str(choice)=='n':
    run('rm -r /usr/share/Erorr ')
    run('rm /usr/bin/Erorr ')
    print('[!] Done install IP Changer Erorr')
