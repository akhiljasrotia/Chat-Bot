from telegram.ext import Updater, CommandHandler

def start(bot, update):
  update.message.reply_text("Hi! My name is Arcanite and I'm your personalized bot :)")



def main():
  # Create Updater object and attach dispatcher to it
  updater = Updater('502538348:AAEIT9TwNtvqF-x_oamoTvRugBvlkHM7yvs')
  dispatcher = updater.dispatcher
  print("Bot started")

  # Add command handler to dispatcher
  start_handler = CommandHandler('start',start)
  dispatcher.add_handler(start_handler)

  # Start the bot
  updater.start_polling()

  # Run the bot until you press Ctrl-C
  updater.idle()

if __name__ == '__main__':
  main()