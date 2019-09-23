#Imports
import praw
import pdb
import re
import os
import time

#Creates authorized Reddit Instance of BAPCSRobot
reddit = praw.Reddit('bot1')
#Creates reference to /r/buildapcsales
subreddit = reddit.subreddit("buildapcsales")
#For keeping track of what posts have been seen already
if not os.path.isfile("posts_visited.txt"):
    posts_visited = []
else:
    with open("posts_visited.txt", "r") as f:
        posts_visited = f.read()
        posts_visited = posts_visited.split("\n")
        posts_visited = list(filter(None, posts_visited))
#Stores posts if they have not been seen already
for submission in subreddit.new(limit=7):
    print(submission.score)
    print(submission.num_comments)
    print(time.time() - submission.created_utc)
    print(submission.title)
    
    #Check to see if a post is marked as expried
    if submission.over_18 or submission.is_self:
        continue
    #If a post has not been added, starts being analyzed
    if submission.id not in posts_visited:
        #Initialize variables
        deal = False
        numcomments = submission.num_comments
        score = submission.score
        if score == 0:
            score = 1
        timepass = time.time() - submission.created_utc
        #Checks to see if a post is getting higher than usual upvotes or comments in a half hour
        if (numcomments > 7 and timepass < 1801) or (score > 15 and timepass < 1801):
            deal = True
        #Checks to see if a post has a much ratio of comments to upvotes in one hour
        if (numcomments / score > 5) or (score / numcomments > 5 and timepass < 3601):
            deal = True
        #If post is found to be a deal, will message my Reddit account and add to visited file
        if (deal):
            print("Found a deal! It's the:\n", submission.title, "\nSending to your Reddit account now!")
            reddit.redditor('RedditUsernameGoesHere').message('(U) [^_^] (U)  Fresh BAPCS Deal! (U) [^_^] (U) ', submission.permalink)
            posts_visited.append(submission.id)
#Writes updated list back to file
with open("posts_visited.txt", "w") as f:
    for post_id in posts_visited:
        f.write(post_id + "\n")
