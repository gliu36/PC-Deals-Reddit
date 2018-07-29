import praw

reddit = praw.Reddit(client_id='j50P1dFZAmUU_g',
                     client_secret='OVOADtNSpXda1oWKGFD6iGrRTek',
                     username='Bot-PC-Deals',
                     password='test123',
                     user_agent='bot for deals')

subreddit = reddit.subreddit('hardwareswap')

new_posts = subreddit.new(limit=4)

for post in new_posts:
    print(post.title)