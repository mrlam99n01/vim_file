import subprocess

p1 = subprocess.run('ls',shell=True)

print(p1.args)

