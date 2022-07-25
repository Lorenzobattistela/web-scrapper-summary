
import scraper

class Controller:
    def buildSummary(self, subject):
        try:
            scrap = scraper.Scraper(subject)
            page = scrap.getWikiPage()
            text = scrap.getText(page)
            formText= scrap.formatText(text)
            title = scrap.getTitle(page)
            file = scraper.File(title)
            created = file.createFile(formText)
            return created
                
        except:
            print("Something went wrong when building your summary")
            return False
    
        
    
