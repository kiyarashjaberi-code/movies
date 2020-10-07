from section_1_1 import read_file_utf8
from bs4 import BeautifulSoup
import re, csv
for file in range(30000):
    film_name ='NA'
    director ='NA'
    producer ='NA'
    writer ='NA'
    starring ='NA'
    music ='NA'
    release_date ='NA'
    runtime ='NA'
    country ='NA'
    language ='NA'
    budget ='NA'
    try:
        data =read_file_utf8('article\\article_{0}.txt'.format(file))
    except:
        continue
    soup =BeautifulSoup(data,'html.parser')
    title =soup.find('h1', attrs={'id':"firstHeading"}).text
    try:
        intro =soup.find_all('p')[0].text
        plot =soup.find_all('p')[1].text
    except:
        continue
    table =soup.find('table', attrs={'class':'infobox vevent'})
    try:
        rows =table.find_all('tr')
        film_name=rows[0].text
        for row in rows:
            if re.search('Directed by',row.text):
                director =row.find('td').text
            if re.search('Produced by',row.text):
                producer =row.find('td').text
            if re.search('Written by',row.text):
                writer =row.find('td').text
            if re.search('Starring',row.text):
                starring =row.find('td').text
            if re.search('Music by',row.text):
                music =row.find('td').text
            if re.search('Release date',row.text):
                release_date =row.find('td').text
            if re.search('Running time',row.text):
                runtime =row.find('td').text
            if re.search('Country',row.text):
                country =row.find('td').text
            if re.search('Language',row.text):
                language =row.find('td').text
            if re.search('Budget',row.text):
                budget =row.find('td').text
    except:
        continue
    d =[title,intro,plot,film_name,director,producer,writer,starring,music,release_date,runtime,country,language,budget]
    with open('tsv\\{0}.tsv'.format(file), 'w', encoding='utf-8', newline ='') as f:
        writer =csv.writer(f, delimiter='\t', )
        writer.writerow(d)
