import socket 
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "chat.freenode.net"
channel = "##idk"
nick = "combo"
admin = "Death916"
logout = "bye " + nick
password = "combo916"
combo = 0
last_nick = ""
exit_code = "!cquit"

def connect():
    sock.connect((server, 6667))
    sock.send(bytes("USER " + nick +" "+ nick + " " + nick + " " + nick + "\n", "UTF-8"))
    sock.send(bytes("NICK " + nick + "\n", "UTF-8" + "\n"))

def auth():
    sock.send(bytes("PRIVMSG" + " NICKSERV :identify " + password +"\n"," UTF-8"))

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

#def combo():
    

def main():
    connect()
    join(channel)
    auth()
    while 1:
        ircmsg = sock.recv(3300).decode("UTF-8")
        ircmsg = ircmsg.strip('\n\r')
        print(ircmsg)
        if ircmsg.find("PRIVMSG") != -1:
            name = ircmsg.split('!',1)[0][1:]
            message = ircmsg.split('PRIVMSG', 1)[1].split(':',1)[1]
            if len(name) < 17:
                global last_nick
                if last_nick != name:
                    global combo
                    combo = 1
                    last_nick = name
                else:
                    if name == last_nick:
                        combo += 1
                       
                if message.find("!combo"):
                    send(name + " is on a " + str(combo) + "combo")
                else:
                    pass
                    
            if name.lower() == admin.lower() and message.rstrip() == exit_code:
                sock.send(bytes("QUIT \n", "UTF-8"))
                return    

            
                    
        if ircmsg.find("PING :") != -1:
            ping()
if __name__ == '__main__':
    main()