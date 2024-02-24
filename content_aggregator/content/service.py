import feedparser
from content.models import Shortcuts

class Feed():
    '''
        TODO: add typing to this file
        
        Being that its pulling from an rss feed the api is standardized
        simply adding a url to URLS should be all that's needed to extend this 
    '''

    URLS = ['https://softskills.audio/feed.xml', 'https://feeds.fireside.fm/bikeshed/rss']
   
    def __init__(self, count=5):
        self.count = count
    
    def helper(self, podcast, label):
            if label == 'link':
               return podcast.link if 'link' in podcast else 'not available'
            elif label == 'title':
               return podcast.title if 'title' in podcast else 'not available'
            elif label == 'summary':
               return podcast.summary if 'summary' in podcast else 'not available'

    def run(self):
        for url in Feed.URLS:
            feed = feedparser.parse(url)
            for idx in range(self.count):
                podcast = feed.entries[idx]
                link = self.helper(podcast ,'link')
                title = self.helper(podcast ,'title')
                summary = self.helper(podcast ,'summary')

                content = Shortcuts(link=link, title=title, summary=summary)
                content.save()


            

    


    
        