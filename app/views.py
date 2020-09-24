from django.shortcuts import render
import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')


Driver_Path = 'Documents\GitHub\BotCodeApp\chromedriver'
#change driver path according to local storage
# from django.http import HttpResponse
# nltk named entity start here
def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    prev = None
    continuous_chunk = []
    current_chunk = []

    for i in chunked:
        if type(i) == Tree:  # extract the markonikov tree
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue
    if current_chunk:
        named_entity = " ".join(current_chunk)
        if named_entity not in continuous_chunk:
            continuous_chunk.append(named_entity)
            current_chunk = []
    return continuous_chunk


def home(request):
    return render(request, 'app/home.html')


def error(request):
    return render(request, 'app/404.html')


def about(request):
    return render(request, 'app/about.html')


def search(request):
    if request.method == 'POST':
        qry_entered = request.POST.get('query')
        # print(qry_entered)
        qry_entered=qry_entered.title()
        named_entity=get_continuous_chunks(qry_entered)
        if(len(named_entity)==0):
            named_entity=qry_entered
        else:
            named_entity=(' ').join(named_entity)
        return render(request, 'app/search.html',
                      {'dict': named_entity, 'wikipedia_result': scrape_wikipedia(qry_entered),'stack_overflow_result':stackoverflow(qry_entered),'general_answer':general_answer(qry_entered,Driver_Path)})
        # {'dict':qry_entered,'search_results_key':scrape_function(qry_entered)})
    else:
        return render(request, 'app/search.html')


def developers(request):
    return render(request, 'app/developers.html')


# wikipedia scrape begins
def scrape_wikipedia(qry):
    import wikipedia

    list_returned = wikipedia.search(qry)  # return a list
    # print(list_returned[0])
    #print(wikipedia.summary(list_returned[0]))
    return wikipedia.summary(list_returned[0])

# wikipedia scrape ends

#stackoverflow scrape begins
headers=dict()
headers["User-Agent"]="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"

def get_ques_text_and_link(q):
    res=requests.get("https://stackoverflow.com/search?q="+q,headers=headers)		#this is exactly the url when we search a question on stack overflow
    soup = BeautifulSoup(res.text, "html.parser")

    questions_data = {
        "questions": []
    }

    question=soup.select_one(".question-summary")
    q=question.select_one('.question-hyperlink')
    link="https://stackoverflow.com"+q["href"]
    ques_text=q.getText()
    print(ques_text)
    print(link)
    return ques_text,link


def get_answer(url):
    #content = urllib.request.urlopen(url)
    source=requests.get(url,headers=headers).text
    soup = BeautifulSoup(source,features='lxml')
    try:
        #answer = soup.find('div',attrs={'class':'accepted-answer'})
        #accepted_content = answer[0].contents[1].find('div',attrs = {'class':'post-text'})
        #accepted_content = answer.find('div',class_="js-post-body")
        accepted_content = soup.find_all('div',class_="js-post-body")
        #print("Detailed Question is :")
        #print(accepted_content[0].text.strip())
        #print("Top Answer is : ")
        #print(accepted_content[1].text.strip())
        return accepted_content[0].text.strip(),accepted_content[1].text.strip()
        #return accepted_content[1].text
    except Exception as error:
        print(str(error))
        return None,'not answered'


def stackoverflow(query):
    ques_text,link=get_ques_text_and_link(query)
    stackoverflow_list=["question is : "+ques_text,"For Details visit : "+link]
    detailed_ques,answer=get_answer(link)
    if(detailed_ques is None):
        return ['The question is not answered in stackoverflow']
    stackoverflow_list.append("Detailed Question : "+ detailed_ques)
    stackoverflow_list.append("Answer is : "+answer)
    return stackoverflow_list
    #[0-quest_text,1-link,2-detailed_ques,3-answer]
#stackoverflow scrape ends

#general_answer scrape begins

def general_answer(q,PATH):
    
    url = f'https://duckduckgo.com/?q={q.lower().replace(" ", "+")}&ia=web'
    #print(url)
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(executable_path=PATH,options = options)

    driver.get(url)

    # prettify the source code and save in source_code
    # soup = BeautifulSoup(driver.page_source, 'html.parser')
    # source_code = soup.prettify()

    # get information if card is present
    try:
        less_btn = driver.find_element_by_class_name("module__toggle--more")
        less_btn.click()
        result_elements = driver.find_elements_by_class_name("module__text")  # use "module__content to get the full card text"
        text = [i.text for i in result_elements]
        #print(*text, sep='\n')
        return text

        # with open('Apoorve/duck-duck-go/card_content.txt', 'w') as outfile:
        # 	outfile.write('\n'.join(text))
        # print('\nOpen card_content.txt')
        #exit()

    except:
        pass

    # if card is not present then collect the short summary provided by the site
    try:
		
        result_elements = driver.find_elements_by_class_name("result__snippet")
        snippets = [i.text for i in result_elements[:5]]
        #print(*snippets, sep='\n')
        return snippets
        # with open('Apoorve/scrape_finalesearch_result_snippets.txt', 'w') as outfile:
        # 	outfile.write('\n'.join(snippets))
        # print('\nOpen search_result_snippets.txt')

    except Exception as e:
        # print(f"Result Error: {e}")
        pass


#general_answer scrape ends
