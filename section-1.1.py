from bs4 import BeautifulSoup
def read_file(file_name):
    """a function to open & read files and return data as a string"""
    text_file = open(file_name)
    data = text_file.read()
    text_file.close()
    return data
def get_links():
    """a function, which pars the files and returns the links as a list"""
    files=['movies1.txt','movies2.txt','movies3.txt'] #a list of files which include links
    links=[]
    for file in files:
        data=read_file(file)
        soup=BeautifulSoup(data,'html.parser')
        file_links=soup.find_all('a') #creating a list which includes file links
        for link in file_links:
            links.append(link.text)
    return links
