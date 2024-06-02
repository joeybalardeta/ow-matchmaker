from core import bot, utils

def main():
    matchmaker_bot = bot.Bot()
    matchmaker_bot.register_commands()
    matchmaker_bot.register_events()
    matchmaker_bot.run()


if __name__ == "__main__":
    main()