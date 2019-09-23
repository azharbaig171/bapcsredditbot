
# BAPCSBot

A Reddit bot using Python and Praw Reddit API wrapper to look for deals on /r/buildapcsales and ping a Reddit account on a hit.

## Goals

One of my favorite pastimes is to window shop PC parts online, and /r/buildapcsales is my main destination. Occasionally, there are really good deals posted that I end up missing from quickly going out of stock for being good deals! I also wanted to pick up both Python and working with a new API.
 
My goal with this bot is to ping a message to my Reddit account when certain deals are found in the new section of the subreddit. The bot is designed to continuously run on a server. In my case, I am using Cron on Ubuntu 18.04 on a Firefly ROC-RK3328-CC development board.

In the future, I would like to add a simple UI to pass in parameters to also return deals on specific types of deals and update the 'deal' method.

## Status
- [x] Correctly configure praw.ini file
- [x] Pull newest posts and check if the have been checked
- [x] Write basic method to determine if a post is a 'deal'
- [x] Setup server for bot
- [ ] Update 'deal' method
- [ ] Add UI to pass parameters for specific deals
- [ ] Add support for tracking more subreddits (???)
- [ ] Add method to deal with Reddit downtime or connection failures

## Running BAPCSRobot
You will need Python 3.7 and will need to install PIP and PRAW
```python
python get-pip.py
pip install praw 
```
To access the Reddit API, you will need to register for access [here](https://www.reddit.com/prefs/apps/).

In order to run the program, you will need to edit the praw.ini file for your own client ID, client secret, username, password, and user_agent. This file will be placed in the current working directory. Here is the section of praw.ini that will need to be modified:

```python
[bot1]
client_id=reddit_client_id
client_secret=reddit_client_secret
password=bot_password
username=bot_username
user_agent=user_agent_name
```
You will also have to edit this line in bapcsrobot.py to add a Reddit username for the bot to PM(This is the only line that needs a Reddit username and password, so you could remove this line from the code and avoid providing a Reddit username and password, but you will still need a client ID, client secret, and user_agent):
```python
 reddit.redditor('RedditUsernameGoesHere').message('(U) [^_^] (U)  Fresh BAPCS Deal! (U) [^_^] (U) ', submission.link)
```

From here, you can run the bot script as-is and it will be functional, but it will not run continuously. To set up automation, you will need a Linux distribution and a few commands ([This site](https://www.pythonanywhere.com) looks like a great simpler alternative, but i found this a little too late...)

To start, you will need to install Python (at least 3.4), pip, PRAW, Git, and clone the repository to the directory of your choosing:

```pyth
sudo apt-get update -y
sudo apt-get install python-pip -y
sudo pip install praw
sudo apt-get install git -y
git clone https://github.com/azharbaig171/bapcsredditbot.git
```
Now, you will have to setup Cron
```python
crontab -e
```
Choose your preferred text editor, and a file will open to add a time and command. To have the program run at a certain path every 2 minutes:
```python
*/2 * * * * cd /Documents/bapcsrobot/bapcsredditbot; ./bapcsrobot.py
```
The bot will now be running in the background. Now you're done!


## Links
[Build a Reddit Bot](https://www.pythonforengineers.com/build-a-reddit-bot-part-1/)

[PRAW Documentation](https://praw.readthedocs.io/en/latest/getting_started/quick_start.html)




## Acknowledgements
Thanks to [this blog post](https://www.pythonforengineers.com/build-a-reddit-bot-part-1/) for a great tutorial on building a Reddit bot and automating the process! 
