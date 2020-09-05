from tkinter import *
import tkinter.messagebox
from tkinter import Tk, FALSE, mainloop
from gingerit.gingerit import GingerIt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    import ttk
from tkcalendar import Calendar
import tweepy as tw
import sqlite3
import datetime


class get_twitter_Data:
    start_date = 0
    end_date = 0
    uName = 'abc'
    screen_name = ""

    def getTwitterData(self, start_date, end_date , u_name):

        self.start_date = start_date
        self.end_date = end_date
        self.uName =u_name
        print(self.uName)
        consumer_key = 'x7eLfHlTsWtGlM4bGvu44qbSl'
        consumer_secret = '6W1hMccZ2DdgL50dgG5xZllDYm705jicJiAkyojNdpcB0ZmUC9'
        access_token = '44594931-pkEBrq9it8ZmViMUHc38QijzNic7rIVabZ6F4tSu8'
        access_token_secret = '9ogPsSvcYYRbQWXHN71j0SasgSgOdLCYTYjfvN8n1y0CK'

        conn = sqlite3.connect('twitterUserData.db')
        c = conn.cursor()
        if not conn:
            print("not connected")
        else:
            print("connected")
            c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='TWEET3'  ''')
            conn.commit()

            # if the count is 1, then table exists
            if c.fetchone()[0] == 1:
                print('Table exists.')
            else:
                print('Table does not exist.')
                c.execute(
                    '''CREATE TABLE TWEET3 (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,NAME TEXT    NOT NULL,Status   INT     NOT NULL,Created_date   TEXT    NOT NULL) ''')
                conn.commit()

        auth = tw.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tw.API(auth, wait_on_rate_limit=True)
        self.screen_name = self.uName
        user_tweet = []
        print(self.start_date)
        print(self.end_date)
        sd = self.start_date
        ed = self.end_date
        text = 'Data collected from ' + str(sd) + ' to ' + str(ed)
        self.label_StarDate = Label(text=text, font=("Helvetica", 15))
        self.label_StarDate.pack()
        endDate = datetime.datetime.combine(ed, datetime.time())
        startDate = datetime.datetime.combine(sd, datetime.time())
        for status in tw.Cursor(api.user_timeline, id=self.screen_name, exclude_replies=True).items(10000):
            if (not status.retweeted) and ('RT @' not in status.text):
                if (status.created_at >= startDate):
                    if (status.created_at <= endDate):
                        user_tweet.append([status.text, status.created_at])
                        # Print Status
                        print('dasdas')
                        print(status.text, ' date ', status.created_at)
                    else:
                        print('no status')
                else:
                    break
        for u_tweets in user_tweet:
            user_status = str(u_tweets[0])
            create_date = str(u_tweets[1])
            c.execute('''INSERT INTO TWEET2 (NAME, Status, Created_date) VALUES (?,?,?)''',
                      (self.screen_name, user_status, create_date))
        conn.commit()
        conn.close()
        self.label_Name = Label(text="finished", font=("Helvetica", 15))
        self.label_Name.pack()