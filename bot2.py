from telegram.ext import *
import downloader
import requests
import re
API_KEY = "1939749981:AAHU4JixeLfiT8GxOVNQLeXWdkNC9oxwCTw"

def start_handler(updater,context):
    updater.message.reply_text("""
    Hi welcome to our bot, for more information please enter /help
    """)

def help_handler(updater,context):
    updtaer.message.reply_text("""
    Here is our commands and message supported!
    1 start
    2 help
    3 video
    """)

def send_video(file,chatID):
    url = "https://api.telegram.org/bot"+API_KEY+"/sendVideo"
    files = {'video':open(file,"rb")}
    data = {"chat_id":chatID}
    recive = requests.post(url,files=files,data=data)
    print(recive.status_code, recive.reason, recive.content)

def message_handler(updater,context):
    text = updater.message.text
    reply_message = ""
    if(text in ("hello","hi","salam")):
        reply_message = "hello world!"
    elif(text in ("how are you","what do you do!")):
        reply_message = "Fine!"
    elif(text.startswith("video")):
        link = re.findall("video (.+)", text)
        send_video(downloader.get_url(link[0]),updater.message.chat.id)
        reply_message = "here is your video"
    updater.message.reply_text(reply_message)

def main():
    updater = Updater(token=API_KEY,use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start_handler))
    dp.add_handler(CommandHandler('help', help_handler))
    dp.add_handler(MessageHandler(Filters.text, message_handler))
    updater.start_polling()
    updater.idle()

if (__name__ == "__main__"):
    main()