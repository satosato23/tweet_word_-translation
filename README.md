# Twitter Translator Bot

This is a simple Twitter bot that searches for recent tweets containing a specific word or hashtag, translates the tweet text into a specified language, and then re-tweets the translated text along with the original tweet's URL.

#Prerequisites
A Twitter account and API keys
Python 3
The tweepy library for Python
The deep_translator library for Python
The dotenv library for Python

#Setup
Create a new Twitter app and obtain your API keys
Clone or download this repository to your local machine
Create a file named ".env" in the root directory and add your API keys and secrets as follows:

Modify the word variable in the code to specify the word or hashtag you want to search for.

#Running the bot
To run the bot, simply execute the script with the following command:

python twitter_translator_bot.py


The bot will search for recent tweets containing the specified word or hashtag, translate them into the specified language, and re-tweet them along with the original tweet's URL. The bot will continue running until you stop it manually.

#Notes
The default language for translation is Japanese, but you can modify the target parameter in the GoogleTranslator object to specify a different language.
The bot will only re-tweet tweets that have been favorited more than 5 times. This can be modified by changing the favorite_count parameter in the if statement.
The bot will pause for 60 seconds after each re-tweet to avoid overloading the Twitter API. This delay can be modified by changing the time.sleep() argument.


