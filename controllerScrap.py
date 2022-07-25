
import scraper
import sys

class Controller:
    def buildSummary(self, subject):
        try:
            scrap = scraper.Scraper(subject)
            page = scrap.getWikiPage()
            text = scrap.getText(page)
            title = scrap.getTitle(page)
            file = scraper.File(title)
            created = file.createFile(text)
            return created
                
        except:
            print("Something went wrong when building your summary")
            return False
        
    
