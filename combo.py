import socket 
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "chat.freenode.net"
channel2 = "##idk"
channel = "#r.trees"
nick = "combo"
admin = "Death916"
logout = "bye " + nick
#password = input('input password\n')
combo = 0
last_nick = ""
exit_code = "!cquit"
start_time = 0

def connect():
    sock.connect((server, 6667))
    sock.send(bytes("USER " + nick +" "+ nick + " " + nick + " " + nick + "\n", "UTF-8"))
    sock.send(bytes("NICK " + nick + "\n", "UTF-8" + "\n"))

"""def auth():
    sock.send(bytes("PRIVMSG" + " NICKSERV :identify " + password +"\n"," UTF-8"))"""

def join(chan):
    sock.send(bytes("JOIN " + chan + "\n", "UTF-8"))
    ircmsg = ""
    while ircmsg.find("End of /NAMES list.") == -1:
        ircmsg = sock.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip('\n\r')
        print(ircmsg)

def ping():
    sock.send(bytes("PONG  :pingis\n", "UTF-8"))

def send(msg, target):
    sock.send(bytes("PRIVMSG " + target + "  :" + msg + "\n", "UTF-8"))


    

def main():
    connect()
    join(channel)
    join(channel2)
    #auth()
    start_time = time.time()
    while 1:
        ircmsg = sock.recv(3300).decode("UTF-8")
        ircmsg = ircmsg.strip('\n\r')
        print(ircmsg)
        if ircmsg.find("PRIVMSG") != -1:
            name = ircmsg.split('!',1)[0][1:]
            message = ircmsg.split('PRIVMSG', 1)[1].split(':',1)[1]
            if len(name) < 17:
                global last_nick
                if last_nick != name and message.rstrip() != "!combo":
                    global combo
                    combo = 1
                    last_nick = name
                else:
                    if name == last_nick:
                        combo += 1
                       
                if message.rstrip() == "!combo":   
                    if combo > 2:
                        send(last_nick + " is on a " + str(combo) + " message streak", channel)
                    elif combo >= 10:
                        send(last_nick + " is on a " + str(combo) + " message streak. they're talkin to themselves", channel)
                        
            if name.lower() == admin.lower() and message.rstrip() == exit_code:
                sock.send(bytes("QUIT \n", "UTF-8"))
                return    

        if ircmsg.find("PING :") != -1:
            ping()

        if time.time() - start_time > 21600:
            sock.send(bytes("PART ##idk\n", "UTF-8"))
            sock.send(bytes("PART #r.trees\n", "UTF-8"))
            print('restart')
            join(channel)
            join(channel2)
            send("restart", channel2)
            start_time = time.time()
            
            
           
            
            
            
if __name__ == '__main__':
    main()
