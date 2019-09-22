# BAPCSBot

A Reddit bot using Python and Praw Reddit API to look for deals on /r/buildapcsales and ping a Reddit account on a hit.

## Goals

One of my favorite pastimes is to window shop PC parts online, and /r/buildapcsales is my main destination. Occasionally, there are really good deals posted that I end up missing from quickly going out of stock for being good deals! I also wanted to pick up both Python and working with a new API.
 
My goal with this bot is to ping a message to my Reddit account when certain deals are found in the new section of the subreddit. The program will scrape the  newest posts on the /r/buildapcsales subreddit every 30 minutes and check to see if the deal is 'good'. The conditions for checking if a deal is 'good' are:


## Status

## Installation
You will need Python installed and will need to install PRAW
```python
pip install praw 
```
To access the Reddit API, you will need to register for access [here](https://www.reddit.com/prefs/apps/).

In order to run the program, you will need your own praw.ini file for your own bot's information. This file will be placed in the current working directory. Here is what a default praw.ini file would look like:

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
client_id=Reddit client ID
client_secret=Reddit client secret
password=Account password
username=Account username
user_agent=User agent name
```


## Usage

## Links

## Acknowledgements
Thanks to [this blog post](https://www.pythonforengineers.com/build-a-reddit-bot-part-1/) for a great tutorial on building a Reddit and providing a place to build from!  
