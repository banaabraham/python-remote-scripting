from netcat import *

host = '192.168.43.44'
port = 4444

remote_computer_python_script = """
for _ in range(5):
    print ("hello world from remote PC")
"""

command =("echo '%s' > run.py;python3 run.py" %(remote_computer_python_script))

s = netcat(host,port,command)

def decoded(s):
    dec = [i.decode().replace("[","").replace("]","").split(",") for i in s]
    res = [i for  i in dec[0]]
    if len(res)==1:
        res = res[0]
    return res

c= decoded(s)    
print(c)
print("hello world from local PC")