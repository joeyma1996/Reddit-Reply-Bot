#Joey's first reddit bot
import praw

keywords = {'love cats'}
bot_phrase = 'I love you too!'

def main():
    #Initialize the Reddit instance using the praw.ini file
    reddit = praw.Reddit('bot2')
    #Choose a subreddit
    subreddit = reddit.subreddit('JoeyMaTest')

    found = 0
    #View the top 10 posts in the hot section
    for submission in subreddit.hot(limit=10):
        if search(submission):
            #At least one post matched a keyword
            found = 1

    #No posts were matched
    if found == 0:
        print()
        print("No posts matching the keyword")

def search(submission):
    lowerTitle = submission.title.lower()

    #Go through keywords to find a match
    for key in keywords:
        #If a match is found, output to command line and replies on reddit
        if key in lowerTitle:
            print('Bot replying to: ')
            print("Title: ", submission.title)
            print("Text: ", submission.selftext)
            print("Score: ", submission.score)
            print("---------------------------------")
            print('Bot saying: ', bot_phrase)
            print()
            submission.reply(bot_phrase)
            return True
    return False

main()