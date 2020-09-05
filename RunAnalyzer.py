import sqlite3
import datetime
import csv
from csv import writer
from gingerit.gingerit import GingerIt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class RunAnalyzer:
    sentences = []

    def run_analyzer(self):
        with open('traindataset.csv', encoding='utf-8') as csvFile, open('output_1.csv', 'w', encoding='utf-8',
                                                                         newline='') as write_obj:
            readCSV = csv.reader(csvFile, delimiter=',')
            csv_writer = writer(write_obj)
            for row in readCSV:
                # print("row ",row)
                getEmotionSentenceList = self.get_emotion(row)
                self.sentences.append(getEmotionSentenceList)
                # print('sentences',sentences)
            for S_lists in self.sentences:
                print("lenght", len(S_lists))
                print(S_lists[1])
                Polarity_Score = S_lists[3]
                sentiment = ""
                polarity_value = 0
                for x in Polarity_Score:
                    print("inside list ", x, "value is ", Polarity_Score[x])
                    if (x == "compound"):
                        if (Polarity_Score[x] >= 0.05):
                            sentiment = "Happy"
                            polarity_value = Polarity_Score[x]
                            print('happy')
                            # self.compoundLabel.configure(text="Result is Happy ")
                        elif (Polarity_Score[x] > -0.05 and Polarity_Score[x] < 0.05):
                            sentiment = "Neutral"
                            polarity_value = Polarity_Score[x]
                            print('neutral')
                            # self.compoundLabel.configure(text="Result is Neutral")
                        elif (Polarity_Score[x] <= -0.05):
                            sentiment = "Sad"
                            polarity_value = Polarity_Score[x]
                            print('sad')
                            # self.compoundLabel.configure(text="Result is Sad")
                S_lists.append(sentiment)
                S_lists.append(polarity_value)
                csv_writer.writerow(S_lists)
            print('sentences', self.sentences)

    def get_emotion(self,sentence):
        # print(sentence[1])
        enteredText = self.checkGrammer(sentence[1])
        sid = SentimentIntensityAnalyzer()
        ss = sid.polarity_scores(enteredText)
        print("score", ss)
        sentence.append(ss)
        # print("sentence", sentence)
        return sentence


    def checkGrammer(self,text):
        # print (text)
        parser = GingerIt()
        item = parser.parse(text)
        return item['result']