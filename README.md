# BAPCSBot

A Reddit bot using Python and Praw Reddit API to look for deals on /r/buildapcsales and ping a Reddit account on a hit.

## Goals

One of my favorite pastimes is to window shop PC parts online, and /r/buildapcsales is my main destination. Occasionally, there are really good deals posted that I end up missing from quickly going out of stock for being good deals! I also wanted to pick up both Python and working with a new API.
 
My goal with this bot is to ping a message to my Reddit account when certain deals are found in the new section of the subreddit. The program will scrape the  newest posts on the /r/buildapcsales subreddit every 15 minutes and check to see if the deal is 'good'. The conditions for checking if a deals is 'good' are:
1. The ratio between upvotes and time
2. The ratio between number of comments and time
3. The ratio between comments and upvotes

If a deal is found to be 'good', not visited before, and not expired, a message will be sent to my Reddit account from the bot's account with the name and link to the posting.

The bot is designed to continuously run on a server. In my case, I am using Cron on Ubuntu 18.04 on a Firefly ROC-RK3328-CC development board.

## Status

## Installation
You will need Python installed and will need to install PRAW
```python
pip install praw 
```
To access the Reddit API, you will need to register for access [here](https://www.reddit.com/prefs/apps/).

In order to run the program, you will need your own praw.ini file for your own client ID, client secret, username, password, and user_agent(Technically, all the bot does is send a message to a Reddit account, so you could remove the bot message code from bapcsrobot.py and avoid providing a Reddit username and password, but you will still need a client ID,secret, and user_agent). This file will be placed in the current working directory. Here is what a default praw.ini file would look like:

```python
[DEFAULT]
# A boolean to indicate whether or not to check for package updates.
check_for_updates=True

# Object to kind mappings
comment_kind=t1
message_kind=t4
redditor_kind=t2
submission_kind=t3
subreddit_kind=t5
trophy_kind=t6

# The URL prefix for OAuth-related requests.
oauth_url=https://oauth.reddit.com

# The URL prefix for regular requests.
reddit_url=https://www.reddit.com

# The URL prefix for short URLs.
short_url=https://redd.it
#This is what will be different based on your own Reddit app and bot information
[bot1]
client_id=reddit_client_id
client_secret=reddit_client_secret
password=bot_password
username=bot_username
user_agent=user_agent_name
```
From here, you can run the bot script as-is and it will be functional, but it will not run continuously. To set up automation, you will need a Linux distribution and a few commands ([This site](https://www.pythonanywhere.com) looks way easier to setup, but i found this a little too late...)

To start, you will need to install pip, praw, Git, and clone the repository.

```pyth
sudo apt-get update -y
sudo apt-get install python-pip -y
sudo pip install praw
sudo apt-get install git -y
git clone https://github.com/azharbaig171/bapcsredditbot.git
```


## Usage

## Links

## Acknowledgements
Thanks to [this blog post](https://www.pythonforengineers.com/build-a-reddit-bot-part-1/) for a great tutorial on building a Reddit bot and automating the process! 
