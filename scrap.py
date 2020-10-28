import fnmatch
import os
from bs4 import BeautifulSoup
import requests


def scrap(url):
  headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'} 
  response=requests.get(url,headers=headers)
  soup = BeautifulSoup(response.content, "html.parser")
  body = []
  for i in soup.find_all(itemprop='articleBody'):
    body.append(i.get_text())
  return " ".join(body)


match_file = fnmatch.filter(os.listdir(os.getcwd()), 'Articles*.csv')
alldfs = {}
for file in match_file:
  data = pd.read_csv(file)
  df = []
  for i in range(len(data['webURL'])):
    df.append([data['articleID'][i],scrap(data['webURL'][i])])
  df = pd.DataFrame(df)
  alldfs.update({file:df})
