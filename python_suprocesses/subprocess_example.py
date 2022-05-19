import subprocess

def sp1Run():
  subprocess.run(['ls', '-l'])

def sp1Call():
  subprocess.call(['ls', '-l'])

def sp1RunWithShellList():
  subprocess.run(['ls', '-l'],shell=True)

def sp1CallWithShellList():
  subprocess.run(['ls', '-l'],shell=True)

def sp1RunWithShellNoList():
  subprocess.run('ls -l',shell=True)

def sp1CallWithShellNoList():
  subprocess.run('ls -l',shell=True)

def returnCode():
  return_code =   subprocess.run('ls -l',shell=True,check=True)
  print(return_code)

def main():
  #sp1Run()
  #p1Call()
  #sp1RunWithShellNoList()
  returnCode()

if __name__ == "__main__":
  main()
