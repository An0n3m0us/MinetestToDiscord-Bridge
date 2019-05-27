import os, sys, time

url = "https://discordapp.com/api/webhooks/582595146634362893/Lrxo0yjvZMRJ6jFUDncgog4NrAqO8k7CN9xFZw946A1NLI_VUWND661Y5dFpN9CTGZ2S"

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
    open(os.path.expanduser('~') + "/.minetest/debug.txt", 'a').close()
    logfile = open(os.path.expanduser('~') + "/.minetest/debug.txt","r")
    loglines = follow(logfile)

    for line in loglines:
        if "] joins game" in line:
            playerJoined = line.split('ACTION[Server]: ')
            playerJoined = playerJoined[1].split(" ")
            #os.system("curl -H \"Content-Type: application/json\" -X POST -d '{ \"embeds\": [ { \"title\": \"" + playerJoined[0] + " has joined the game\"} ] }' " + url)
            os.system("curl -H \"Content-Type: application/json\" -X POST -d '{\"username\": \"Minetest\", \"content\": \"" + playerJoined[0] + " has joined the game\"}' " + url)
        if "leaves game" in line:
            playerLeft = line.split('ACTION[Server]: ')
            playerLeft = playerLeft[1].split(" ")
            #os.system("curl -H \"Content-Type: application/json\" -X POST -d '{ \"embeds\": [ { \"title\": \"" + playerLeft[0] + " has left the game\"} ] }' " + url)
            os.system("curl -H \"Content-Type: application/json\" -X POST -d '{\"username\": \"Minetest\", \"content\": \"" + playerLeft[0] + " has left the game\"}' " + url)
        if "CHAT:" in line:
            chat = line.split("CHAT: ")
            chat = chat[1].split("> ")
            chat = chat[0] + ">: " + chat[1]
            chat = chat.rstrip()
            os.system("curl -H \"Content-Type: application/json\" -X POST -d '{\"username\": \"Minetest\", \"content\": \"" + chat + "\"}' " + url)

        if "Server: Shutting down" in line:
            sys.exit()
