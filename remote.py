from netcat import netcat
import threading

host = '192.168.43.44'
port = 4444

script = """
print(" world")
"""
class remote_run:
    def __init__(self,host,port):
        self.host = host
        self.port = port
    def send_command(self,script):
        self.script = script
        self.command = ("echo '%s' > run.py;python3 run.py" %(script))
        self.result = netcat(self.host,self.port,self.command)
        dec = [i.decode().replace("[","").replace("]","").split(",") for i in self.result]
        res = [i for  i in dec[0]]
        if len(res)==1:
            res = res[0]
        print (res+"\r") 
def print_str(s):
    print (s,end="")
    
remote_computer = remote_run("192.168.43.44",4444)

#print "hello" on local computer and "world" on remote computer 
t_1 = threading.Thread(target=remote_computer.send_command, args=(script,))
t_2 = threading.Thread(target=print_str, args=("hello",))
t_1.start()
t_2.start()
t_1.join()
t_2.join()
