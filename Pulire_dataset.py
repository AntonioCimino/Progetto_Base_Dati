import pandas as pd
import csv

def delete_img_null():
    news = pd.read_csv("fake_news_dataset.csv")
    news.dropna(subset=['text', 'title','author','country','language','site_url','published','main_img_url'])

    with open('fake_news_dataset_not_null.csv', 'w',encoding= "UTF-8" ,newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(["uuid","ord_in_thread","author","published","title",
                        "text","language","crawled","site_url","country",
                        "domain_rank","thread_title","spam_score","main_img_url","replies_count",
                        "participants_count","likes","comments","shares","type"])

        for i in range (0,len(news)):
            try:
                writer.writerow([news["uuid"][i], news["ord_in_thread"][i], news["author"][i], news["published"][i], news["title"][i],
                             news["text"][i], news["language"][i], news["crawled"][i], news["site_url"][i], news["country"][i],
                             news["domain_rank"][i], news["thread_title"][i], news["spam_score"][i], news["main_img_url"][i], news["replies_count"][i],
                             news["participants_count"][i], news["likes"][i], news["comments"][i], news["shares"][i], news["type"][i]
                ])
            except:
                print("ERRORE")


delete_img_null()