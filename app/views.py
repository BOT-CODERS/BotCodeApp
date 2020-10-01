from django.shortcuts import render
from django.http import JsonResponse

import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

from . import wiki_answer as wiki
from . import general_answer as gen
from . import stackoverflow as stack

import platform

nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')

OS = platform.system()
if(OS == "Linux") :
	Driver_Path = "app/Linux/chromedriver"

elif(OS == "Windows"):
	Driver_Path = "app/Win/chromedriver"

# change driver path according to local storage
# from django.http import HttpResponse
# nltk named entity start here
def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
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
        site = request.POST.get('site')

        qry_entered = qry_entered.title()
        named_entity = get_continuous_chunks(qry_entered)
        if (len(named_entity) == 0):
            named_entity = qry_entered
        else:
            named_entity = (' ').join(named_entity)
            
         
        result_dict = {'dict': named_entity}
        
        site_dict = {'ans': gen.general_answer(qry_entered, Driver_Path), 'site': 'General'} if site=='1' else\
                     {'ans': wiki.scrape_wikipedia(qry_entered), 'site': 'Wikipedia'} if site=='2' else\
                     {'ans': stack.stackoverflow(qry_entered), 'site': 'StackOverflow'}

        result_dict.update(site_dict)
        return JsonResponse(result_dict)
        # {'dict':qry_entered,'search_results_key':scrape_function(qry_entered)})
    else:
        return render(request, 'app/search.html')


def developers(request):
    return render(request, 'app/developers.html')


