import os, sys, time, subprocess

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
    # Log file
    open(os.path.expanduser('~') + "/.minetest/debug.txt", 'a').close()
    logfile = open(os.path.expanduser('~') + "/.minetest/debug.txt","r")
    loglines = follow(logfile)

    for line in loglines:
        # Initialization of game
        if "] joins game" in line:
            playerJoined = line.split('ACTION[Server]: ')
            playerJoined = playerJoined[1].split(" ")
            os.system("curl -H \"Content-Type: application/json\" -X POST -d '{ \"embeds\": [ { \"title\": \"" + playerJoined[0] + " has joined the game\"} ] }' https://discordapp.com/api/webhooks/582561614130053120/BjSVJiT7HL2K8y5wsIOZggTCMG4SB-bBa8rNiBznQHRBYlFtoCWU5Je5j40vAbBAoVdH")
        if "leaves game" in line:
            playerLeft = line.split('ACTION[Server]: ')
            playerLeft = playerLeft[1].split(" ")
            os.system("curl -H \"Content-Type: application/json\" -X POST -d '{ \"embeds\": [ { \"title\": \"" + playerLeft[0] + " has left the game\"} ] }' https://discordapp.com/api/webhooks/582561614130053120/BjSVJiT7HL2K8y5wsIOZggTCMG4SB-bBa8rNiBznQHRBYlFtoCWU5Je5j40vAbBAoVdH")
        if "CHAT:" in line:
            chat = line.split("CHAT: ")
            chat = chat[1].split("> ")
            chat[0] = chat[0][1:]
            chat = chat[0] + ": " + chat[1][:-1]
            os.system("curl -H \"Content-Type: application/json\" -X POST -d '{\"username\": \"Minetest\", \"content\": \"" + chat + "\"}' https://discordapp.com/api/webhooks/582561614130053120/BjSVJiT7HL2K8y5wsIOZggTCMG4SB-bBa8rNiBznQHRBYlFtoCWU5Je5j40vAbBAoVdH")

        if "Server: Shutting down" in line:
            sys.exit()
