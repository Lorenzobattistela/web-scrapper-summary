# import required modules
import datetime
from bs4 import BeautifulSoup
import requests
from os.path import exists as file_exists

class Scraper:
    def __init__(self, subject) -> None:
        self.subject = subject

    def getWikiPage(self):
        return requests.get(f"https://en.wikipedia.org/wiki/{self.subject}")

    def getText(self, page):
        soup = BeautifulSoup(page.content, 'html.parser')
        list(soup.children)
        paragraphs = soup.find_all('p')
        text = ''
        for paragraph in paragraphs:
            text += f'{paragraph.get_text()}\n'
        return text

    def getTitle(self, page):
        soup = BeautifulSoup(page.content, 'html.parser')
        title = (soup.find('title').get_text()).split()
        fileTitle = f'{title[0]}{title[1]}'
        return fileTitle

class File:
    def __init__(self, title) -> None:
        self.creationDate = datetime.datetime.now()
        self.databasePath = f'./database/{title}.txt'

    def createFile(self, text):
        try:
            if self.checkFileExists() == True:
                print('File already exists')
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
