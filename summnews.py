from bs4 import BeautifulSoup
from collections import Counter
import math
import nltk
from nltk.corpus import stopwords
from nltk import probability
import requests
import time
from tqdm import tqdm

class SummNews:
    def __init__(self, sent_num, article_num=0, shakespeare=False):
        self.sent_num = sent_num
        self.article_num = article_num
        self.shakespeare = shakespeare

        #self.start_up() / self.get_summed_news()

    def get_clean_tokens(self, text, is_elizabethan=False):
        tokenizer = nltk.tokenize.RegexpTokenizer("[A-Za-z]\w+")

        # Credit to http://bryanbumgardner.com/elizabethan-stop-words-for-nlp/ for the following Elizabethan stopword list.
        elizabethan_stopwords = ["art", "doth", "dost", "ere",
                                 "hast", "hath", "hence", "hither",
                                 "nigh", "oft", "st", "thither",
                                 "tither", "thee", "thou", "thine",
                                 "thy", "tis", "twas", "wast",
                                 "whence", "wherefore", "whereto", "withal",
                                 "ye", "yon", "yonder"]

        word_tokens = tokenizer.tokenize(text)

        words = []
        for word in word_tokens:
            if (word.lower() not in stopwords.words("english") and
                word.lower() not in elizabethan_stopwords):
                words.append(word.lower())

        return words

    def get_shakespeare_text(self):
        file = open("data/ReadingNet_shakespeare.txt")
        shake_text = file.read()
        file.close()

        return shake_text

    def get_bbc_articles(self, n):
        request_url = "http://www.bbc.com"

        response = requests.get(request_url + "/news")
        soup = BeautifulSoup(response.text, "html.parser")
        headlines = soup.find_all("a", "gs-c-promo-heading")

        articles = []

        print("Getting BBC articles.")

        loop_length = len(headlines) if n == 0 or n > len(headlines) else n
        for i in tqdm(range(loop_length)):
            if "/news/" in headlines[i].attrs["href"] and "https" not in headlines[i].attrs["href"]:
                response = requests.get(request_url + headlines[i].attrs["href"])
                soup = BeautifulSoup(response.text, "html.parser")

                try:
                    main_body = soup.find("div", class_="story-body")
                    bodies = main_body.find("div", {"property": "articleBody"})
                    body_ps = bodies.find_all("p")

                    article_title = main_body.find("h1", class_="story-body__h1").text
                    article_body = "\n".join([ps.text for ps in body_ps])

                    if len(article_title) > 0 and len(article_body) > 0:
                        articles.append({"title": article_title, "body": article_body})
                except:
                    pass

        return articles

    def score_sort_sentences(self, sentences, freq_count):
        scores = [0.0] * len(sentences)
        for idx, sentence in enumerate(sentences):
            scores[idx] = 0.0
            for word in nltk.word_tokenize(sentence):
                if word in freq_count: scores[idx] += (freq_count[word] / len(freq_count))

        sorted_scores = sorted(scores, key=float, reverse=True)

        return scores, sorted_scores

    def summerize_to_sentence_num(self, sentences, scores, sorted_scores,
                                  num_sentences, include_first_sentence=False):
        summ_sentence_list = []
        min_score = sorted_scores[num_sentences-1] if len(sorted_scores) >= num_sentences else sorted_scores[-1]
        for idx, score in enumerate(scores):
            if (idx == 0 and include_first_sentence):
                summ_sentence_list += [sentences[idx]]
            elif score > min_score:
                summ_sentence_list += [sentences[idx]]

        return summ_sentence_list

    def summarize_articles(self, articles):
        summed_articles = []

        print("Summarizing articles.")

        for article in tqdm(articles):
            article_sents = nltk.sent_tokenize(article["body"])

            article_tokens = self.get_clean_tokens(article["body"])
            article_wordcounts = Counter(article_tokens)

            scores, scores_sorted = self.score_sort_sentences(article_sents, article_wordcounts)
            summarization = self.summerize_to_sentence_num(article_sents, scores, scores_sorted, self.sent_num)

            summed_article = {"title": article["title"], "body": " ".join(summarization)}

            summed_articles.append(summed_article)

        return summed_articles

    def get_summed_news(self):
        articles = self.get_bbc_articles(self.article_num)

        if len(articles) <= 0:
            return "No articles were found."

        summed_articles = self.summarize_articles(articles)

        #for summed_article in summed_articles:
        #    print("\n\n* " + summed_article["title"] + " *\n" +
        #          summed_article["body"])

        return summed_articles

#shake_wordcounts = Counter(get_clean_tokens(get_shakespeare_text(), is_elizabethan=True))
#shake_scores, shake_scores_sorted = score_sort_sentences(article_sent_tokens, shake_wordcounts)
#shake_summerization = summerize_to_sentence_num(article_sent_tokens, shake_scores,
#                                                shake_scores_sorted, 5,
#                                                include_first_sentence=True)
#
#print(articles[0]["title"] + "\n\n" + " ".join(shake_summerization))
