import pandas as pd
import csv

def delete_img_null():
    news = pd.read_csv("fake_news_dataset.csv")
    news.dropna(axis='index', how='any', inplace=True)

    '''
    news = list(zip(
        news.uuid.values,news.ord_in_thread.values,news.author.values,news.published.values,news.title.values,
        news.text.values,news.language.values,news.crawled.values,news.site_url.values,news.country.values,
        news.domain_rank.values,news.thread_title.values,news.spam_score.values,news.main_img_url.values,
        news.replies_count.values,news.participants_count.values,news.likes.values,news.comments.values,
        news.shares.values,news.type.values
    ))
    '''

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