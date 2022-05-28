from pexpect import pxssh

def send_command(s, cmd):
        s.sendline(cmd)
        s.prompt()
        print( s.before)

def connect(user, host, password):
        try:
                s = pxssh.pxssh()
                s.login(host, user, password)
                return s
        except:
                print ('[-] Error Connecting')
                exit(0)

def main():
        host = '192.168.29.130'
        user = 'ubuntu'
        password = 'ubuntu'
        s = connect(user, host , password)
        send_command(s, 'cat /etc/shadow | grep root | ls -a')

if __name__ == '__main__':
        main()