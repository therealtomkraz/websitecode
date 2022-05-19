import subprocess

#Run a process and output goes to sceen only
def spRun():
  subprocess.run(['ls', '-l'])

#Same as above only using call instead of Run. 
#Run is the prefered method
def spCall():
  subprocess.call(['ls', '-l'])

#run the command with a shell.
#this does not run the '-l'
def spRunWithShellListShell():
  subprocess.run(['ls', '-l'],shell=True)

#This works just fine
def spRunWithShellNoListshell():
  subprocess.run('ls -l',shell=True)

#Get the return code from a process
def spReturnCode():
  return_code =   subprocess.run('ls -l',shell=True,check=True)
  print(return_code)

#Capute the output and print
def spCaptureOutput():
  cmd_output = subprocess.run('ls -l /', shell=True,capture_output=True)
  print(cmd_output.stdout.decode())

def main():
  spCaptureOutput()

if __name__ == "__main__":
  main()
