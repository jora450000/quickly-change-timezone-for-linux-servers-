#!/usr/bin/python
# -*- coding: utf-8 -*-

#import wx
import paramiko
data = ''

def  MakeTashkent(host, user, pswd):
  port = 22
	client1 = paramiko.SSHClient()
	client1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client1.connect(hostname=host, username=user, password=pswd, port=port)
	
        

  # need, if your / is in read-only mode
  stdin, stdout, stderr = client1.exec_command('mount -o remount,rw /')
	data = stdout.read() + stderr.read()
  print data


  tdin, stdout, stderr = client1.exec_command('rm -f /etc/localtime')
	data = stdout.read() + stderr.read()
  print data


  # set your timezone file symlink here - my is GMT+05:00
  tdin, stdout, stderr = client1.exec_command('ln -s /usr/share/zoneinfo/Asia/Tashkent /etc/localtime')
	data = stdout.read() + stderr.read()
  print data
	client1.close()


 


    
def main():
    
    MakeTashkent("webserver1.local", "root", "password")



if __name__ == '__main__':
    main()
