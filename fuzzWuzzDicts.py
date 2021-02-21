# -*- coding: utf-8 -*-

diction = [
    {"name": "Good morning.", "time": "00:00:14"},
    {
        "name": "So today we will start discussing about the first model of our course.",
        "time": "00:00:16",
    },
    {"name": "Which will be dealing with the.", "time": "00:00:23"},
    {"name": "Functions.", "time": "00:00:25"},
    {"name": "The importance regulations.", "time": "00:00:27"},
]

summary = """</font></i></p><p> . . ?    discussing</i></p><p> about...?.   '<br/> <br/></p>"""

from bs4 import BeautifulSoup
import re
from fuzzywuzzy import process
import itertools

time_list = []
sentence_list = []
for sentence in diction:
    time_list.append(sentence['time'])
    sentence_list.append(sentence['name'])
dict_dict = dict(zip(time_list, sentence_list))

print("Summary: ", summary)
soup = BeautifulSoup(summary,features="html.parser")
cleansummary = re.sub('\W+',' ', soup.get_text())
cleansummary = cleansummary.strip()
# cleansummary = " ".join(soup.get_text().split()) #remove multiple empty spaces
# s = re.sub("\s\s+", " ", s)
print("CleanSummary: ", cleansummary)

matches = process.extract(cleansummary, dict_dict, limit=3)
# print("matches", matches)

sentences = [matches[n][0] for n in range(len(matches))]
# print(sentences)

scores = [matches[n][1] for n in range(len(matches))]
# print(scores)
# 
timestamp = [matches[n][2] for n in range(len(matches))]
# print(index)

threshold = 85
if scores[0] > threshold:
    result_sentences = [ _ for _ in itertools.compress(sentences, map(lambda x: x>=threshold , scores)) ] # iterate the result.
    print(result_sentences)
    result_timestamp = [ _ for _ in itertools.compress(timestamp, map(lambda x: x>=threshold , scores)) ] # iterate the result.
    print(result_timestamp)

else:
    print("no match found")
