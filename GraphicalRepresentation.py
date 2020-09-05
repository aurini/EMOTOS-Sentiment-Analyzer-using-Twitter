import pandas as pd
import sns as sns
from textblob import TextBlob
from itertools import islice
import matplotlib.pyplot as plt


class GraphicalRepresentation:

    def representation(self):
        df_survey_data = pd.read_csv("data.csv")

        COLS = ['date', 'text', 'sentiment', 'subjectivity', 'polarity']

        df = pd.DataFrame(columns=COLS)
        for index, row in islice(df_survey_data.iterrows(), 0, None):
            new_entry = []
            print(row['Responses'])
            text_lower = row['Responses']
            blob = TextBlob(text_lower)
            sentiment = blob.sentiment

            polarity = sentiment.polarity
            subjectivity = sentiment.subjectivity
            print(row['Date'])
            new_entry += [row['Date'], text_lower, sentiment, subjectivity, polarity]

            single_survey_sentimet_df = pd.DataFrame([new_entry], columns=COLS)
            df = df.append(single_survey_sentimet_df, ignore_index=True)

        df.to_csv('Q7_Text_Sentiment_Values.csv', mode='w', columns=COLS, index=False, encoding="utf-8")
        dffilter = df.loc[(df.loc[:, df.dtypes != object] != 0).any(1)]
        df_sentiment_data = pd.read_csv('Q7_Text_Sentiment_Values.csv')
        date_polarity = df_sentiment_data['date']
        data_polarity = df_sentiment_data['polarity']
        plt.plot(date_polarity, data_polarity)
        plt.xlabel('Date')
        plt.ylabel('Polarity')
        plt.show()
        print(df.describe())
        print(dffilter.describe())
