import wikipediaapi
from . import general_answer as gen
import platform
# wikipedia scrape begins
def scrape_wikipedia(qry):
	wiki_wiki = wikipediaapi.Wikipedia('en')
	page_py = wiki_wiki.page(qry)
	
	if page_py.exists():
		return page_py.summary
		
	else:
		OS = platform.system()
		if(OS == "Linux") :
			Driver_Path = "app/Linux/chromedriver"

		elif(OS == "Windows"):
			Driver_Path = "app/Win/chromedriver"

		general_res = gen.general_answer(qry, Driver_Path)
		return general_res
	
