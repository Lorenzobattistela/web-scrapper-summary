
import gui
import scraper
import sys

class Controller:
    def initGui(self, gui_type="desktop"):
        if gui_type == "desktop":
            gui.main()
    
    def buildSummary(self, subject):
        # calls model here
        try:
            scrap = scraper.Scraper(subject)
            page = scrap.getWikiPage()
            text = scrap.getText(page)
            title = scrap.getTitle(page)
            file = scraper.File(title)
            created = file.createFile(text)
                
        except:
            print("Something went wrong when building your summary")
        
    
a = Controller()
a.buildSummary("Michael_Jordan")
    

