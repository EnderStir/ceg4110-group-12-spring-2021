# This file is needed to keep the bot from shutting down when no one who has access to the code does not
# have it pulled up, as repl.it gives the code a 1 minute runtime limit after all users exit the ide.
# It creates a server on repl.it which can then be connected to the host, in this case uptime robot,
# which will then keep the code running and connected indefinitely.
# Reference: https://replit.com/talk/learn/my-bot-goes-down-every-minute-and-doesn/11008/150912
from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def main():
    return "Your bot is alive"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_bot_alive():
    server = Thread(target=run)
    server.start()