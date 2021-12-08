#from ftplib import FTP
import ftplib

host = '127.0.0.1'

ftp = ftplib.FTP(timeout=5)

def loginFTP(host,port=21):
    # si no hay port va directo al 21
    try:
        ftp.connect(host,port)
        try:
            if ftp.login("anonymous","anonymous"):
                print("Default credentials in "+host+":"+str(port))
                saveOutput(host,port)
                ftp.close()
        except ftplib.all_errors:
            print ("Error logging in to "+host+":"+str(port))
    except ftplib.all_errors:
        print("Error connecting to "+host+":"+str(port))

def loginFileTarget(filePath):
    separator = ":"
    with open(filePath, 'r') as ip:
        for line in ip:
            if ":" in line:
                values = line.rstrip('\n').split(":")
                loginFTP(values[0],int(values[1]))
                print (values[0]+" "+values[1])
            else:
                loginFTP(line.rstrip('\n'))
                print(line.rstrip('\n'))

def saveOutput(host,port):
    f = open("ftpAnon.txt","a")
    f.write(host+":21/TCP\n")
    f.close()

loginFileTarget("/home/alux/github/scanTool/ips.txt")