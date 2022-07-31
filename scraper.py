# import required modules
import datetime
import re
from bs4 import BeautifulSoup
import requests
from os.path import exists as file_exists

class Scraper:
    def __init__(self, subject) -> None:
        self.subject = subject
        
    def getGoogleScholarPage(self):
        subj = self.subject.replace(" ", "+")
        return requests.get(f"https://scholar.google.com/scholar?hl=en&q={subj}")

    def getWikiPage(self):
        subj = self.subject.replace(" ", "_")
        return requests.get(f"https://en.wikipedia.org/wiki/{subj}")

    def getText(self, page):
        soup = BeautifulSoup(page.content, 'html.parser')
        list(soup.children)
        paragraphs = soup.find_all('p')
        text = ''
        for paragraph in paragraphs:
            text += f'{paragraph.get_text()}\n'
        return text

    def formatText(self, text):
        formatted_text = re.sub(r'[\[]\d{1,}[\]]', '', text)
        return formatted_text

    def getTitle(self, page):
        soup = BeautifulSoup(page.content, 'html.parser')
        title = (soup.find('title').get_text()).split()
        fileTitle = f'{title[0]}'
        return fileTitle
    
    def getLinks(self, page):
        links = []
        soup = BeautifulSoup(page.content, 'html.parser')
        for link in soup.find_all('a', 
            attrs={'href': re.compile("^https://books.google.com")}):
            links.append(link.get('href'))  
        return links
        

class File:
    def __init__(self, title) -> None:
        self.creationDate = datetime.datetime.now()
        self.databasePath = f'./database/{title}.txt'

    def createFile(self, text):
        try:
            if self.checkFileExists() == True:
                return True
            file = open(f'{self.databasePath}', 'w+')
            file.write(text)
            file.close()
            return True
        except IOError:
            print('Something got wrong when writing your file.')
            return False
        
    def checkFileExists(self):
        return file_exists(self.databasePath)
