import praw
from win10toast import ToastNotifier
import time
import webbrowser

SUBREDDIT = 'mechmarket'
SCRAPE_TERMS = ['holy', 'panda', 'pandas', 'satisfaction']

reddit = praw.Reddit(client_id='j50P1dFZAmUU_g',
                     client_secret='OVOADtNSpXda1oWKGFD6iGrRTek',
                     username='Bot-PC-Deals',
                     password='test123',
                     user_agent='bot for deals')

notification = ToastNotifier()
start_time = time.time()

for post in reddit.subreddit(SUBREDDIT).stream.submissions():
    if post.created_utc > start_time:
        if any(term in post.title.lower() for term in SCRAPE_TERMS):
            print(post.title, post.url)
            notification.show_toast(post.title, post.url, duration=3)
            webbrowser.open_new_tab(post.url)
            with open('posts.txt', 'a+', encoding="utf-8") as file:
                file.write(post.title + ", Link: " + post.url + "\n")