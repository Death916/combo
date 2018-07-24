import socket 
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "chat.freenode.net"
channel = "##idk"
nick = "combo"
admin = "Death916"
logout = "bye " + nick
password = "combo916"

def connect():
    sock.connect((server, 6667))
    sock.send(bytes("USER " + nick +" "+ nick + " " + nick + " " + nick + "\n", "UTF-8"))
    sock.send(bytes("NICK " + nick + "\n", "UTF-8" + "\n"))
    sock.send("PRIVMSG" + " NICKSERV :identify " + password +"\n")

def join(chan):
    sock.send(bytes("JOIN " + chan + "\n", "UTF-8"))
    ircmsg = ""
    while ircmsg.find("End of /NAMES list.") == -1:
        ircmsg = sock.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip('\n\r')
        print(ircmsg)

def ping():
    sock.send(bytes("PONG  :pingis\n", "UTF-8"))

def send(msg, target=channel):
    sock.send(bytes("PRIVMSG " + target + "  :" + msg + "\n", "UTF-8"))

def combo():
    s

def main():
    connect()
    join(channel)
    while 1:
        ircmsg = sock.recv(3300).decode("UTF-8")
        ircmsg = ircmsg.strip('\n\r')
        print(ircmsg)
        if ircmsg.find("PRIVMSG") != -1:
            name = ircmsg.split('!',1)[0][1:]
            message = ircmsg.split('PRIVMSG', 1)[1].split(':',1)[1]
            if len(name) < 17:
                if message.find():
                    pass
        if ircmsg.find("PING :") != -1:
             ping()
        
