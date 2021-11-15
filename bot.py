import googletrans, telegram.ext
from googletrans import Translator

translator = Translator()

with open("token.txt", "r") as token:
	TOKEN = token.read()

def translating(text):
	trans_text = translator.translate(text)
	return trans_text

def start(update, context):
	update.message.reply_text("Hello, welcome to Daquiver's Language Translator ")
#print(googletrans.LANGUAGES)

def handle_message(update, context):
	update.message.reply_text(f"You typed {update.message.text} and the transaltion is {translating(update.message.text)} ")


updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))


updater.start_polling()
updater.idle()




# With googletrans the methods are
# translate
# detect
# LANGUAGES