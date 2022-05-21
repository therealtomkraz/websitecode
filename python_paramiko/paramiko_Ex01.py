import paramiko

hostname = '192.168.186.150'
username = 'testuser'
password = 'testuserpassword'
port = 22

#Return an ssh connection
def SSHClient():
  #Create a ssh Client Class
  sshClient = paramiko.SSHClient()

  #Auto approve Adding the Hostkey.
  sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())

  #Do the connection
  sshClient.connect(
    hostname=hostname,
    username=username,
    port=22,
    password=password
    )
  return sshClient

def runRemoteCommand(command):
  sshClient = SSHClient()
  stdin, stdout, stderr = sshClient.exec_command(command)
  return stdout.readlines()


if __name__ == '__main__':
  cmdOutput = runRemoteCommand('cat /etc/passwd')

  for i in cmdOutput:
    print(i.strip())
