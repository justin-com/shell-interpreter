import subprocess

while True:
    cmd = input("$ ")
    if cmd.lower() == "exit":
        break
    
    subprocess.run(cmd, shell=True)