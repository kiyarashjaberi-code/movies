import requests, time, random
from bs4 import BeautifulSoup
from section_1_1 import get_links, read_file
def get_sourse():
    """ this function gets an html source of the links and saves them as a text file. """
    links=get_links()
    for link in range(len(links)):
        time.sleep(random.randrange(1,3))
        try:
            res=requests.get(links[link])
            with open('article\\article_{0}.txt'.format(link),'w',encoding="utf-8") as f:
                f.write(res.text)
                f.close()
        except:
            pass
get_sourse()