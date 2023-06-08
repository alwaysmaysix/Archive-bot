import os
from pyrogram import Client
from os import mkdir

app_id = '18443762'
app_key = 'a14eb15b00ffaa1f54a7bf93cd521e92'
token =  '6214452248:AAFs_yAKjPGeLyI58u_Q_86e1JrA_aiB-hQ'

app = Client("zipBot", app_id, app_key, bot_token=token)


if __name__ == '__main__':

    try:
        mkdir("static")  # create static files folder
    except FileExistsError:
        pass

    app.run()
