#Code examples for shlex

#Split a string to a list
import shlex
def shlexEx01():
  s = 'uname -r'
  print(shlex.split(s))
  
#Split a string to a list and use it in subprocess
def shlexEx02():
  import subprocess

  command =  'grep 127.0.0.1 /etc/hosts'
  commandList = shlex.split(command)
  subprocess.run(commandList)

#Using shlex to add quotes to commands to prevent command injection
def shlexE03():
  filename = shlex.quote('/tmp;whoami')
  command = f"ls -l {filename}"
  print(command)

def main():
  #shlexEx01()
  #shlexEx02()
  shlexE03()

if __name__ == '__main__':
  main()
