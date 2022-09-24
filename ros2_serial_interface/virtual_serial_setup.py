from os import system
def main(args=None):
    system('socat -d -d pty,link=/dev/ttyS0,raw,echo=0 pty,link=/dev/ttyS1,raw,echo=0 &') #setup serial server
    system('socat -d -d pty,link=/dev/ttyS2,raw,echo=0 pty,link=/dev/ttyS3,raw,echo=0 &') #setup serial client
if __name__ == '__main__':
	main()