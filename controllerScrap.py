
import scraper

class Controller:
    def buildSummary(self, subject):
        try:
            scrap = scraper.Scraper(subject)
            wikiPage = scrap.getWikiPage()
            text = scrap.getText(wikiPage)
            formText= scrap.formatText(text)
            title = scrap.getTitle(wikiPage)
            file = scraper.File(title)
            
            gscholarPage = scrap.getGoogleScholarPage()
            links = scrap.getLinks(gscholarPage)
            
            completeText = "Here are some article links that I found about this subject: \n"
            for link in links:
                completeText += link
                completeText += "\n"
            completeText += formText
            
            created = file.createFile(completeText)
            return created
                
        except:
            print("Something went wrong when building your summary")
            return False
    
        
    
