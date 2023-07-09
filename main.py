import os
from pyrogram import Client
from os import mkdir

app_id = '18443762'
app_key = 'a14eb15b00ffaa1f54a7bf93cd521e92'
token =  '5552172781:AAEjI-y92ZYMRajYz4y1EnvrQ4HAwEd2ZIA'

app = Client("zipBot", app_id, app_key, bot_token=token)


if __name__ == '__main__':

    try:
        mkdir("static")  # create static files folder
    except FileExistsError:
        pass

    app.run()
