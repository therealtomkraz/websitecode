import paramiko

#Set up Variables
hostname = '192.168.186.150'
username = 'testuser'
password = 'testuserpassword' #Not used
ssh_priv_key = '/home/tomkraz/.ssh/id_rsa'

#Return an ssh connection
def SSHClient():
  #Create ssh client Object
  sshClient = paramiko.SSHClient()

  #Auto approve Adding the Hostkey.
  sshClient.set_missing_host_key_policy(
      paramiko.AutoAddPolicy()
      )

  #Connect to remote server
  sshClient.connect(
    hostname=hostname,
    username=username,
    key_filename=ssh_priv_key
    )

  return sshClient

#Run command, print output and return output
def runRemoteCommand(command='ls -l /'):
  sshClient = SSHClient()

  #stdin, stdout and stderr are returned as output
  stdin, stdout, stderr = sshClient.exec_command(command)

  #Output is returned as list so we have to itterate
  for i in stdout: 
    print(i.strip())

#Copy a file from a remote server
def copyFromRemote():
  sshClient = SSHClient() #sshClient 
  sftpClient = sshClient.open_sftp() #sftpClient

  #Get file from remote server
  sftpClient.get('/etc/hosts', '/tmp/hosts_get_test')

#Copy a file to a remote server
def copyToRemote():
  sshClient = SSHClient() #sshClient 
  sftpClient = sshClient.open_sftp() #sftpClient

  #Put a file onto a remote server
  sftpClient.put('/etc/hosts', '/tmp/hosts_put_test')

if __name__ == '__main__':
  #copyToRemote()
  #copyFromRemote()
  #runRemoteCommand()

