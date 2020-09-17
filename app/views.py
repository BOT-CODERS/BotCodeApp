from django.shortcuts import render
import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
#from django.http import HttpResponse
#import nltk
def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))  
    prev = None
    continuous_chunk = []
    current_chunk = []

    for i in chunked:
        if type(i) == Tree:  #extract the markonikov tree 
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
    return render(request,'home.html') 

def add(request):
    query=request.GET['query']
    res=get_continuous_chunks(query)
    return render(request,"result.html",{"result":res})

def search(request):
    if request.method=='POST':
        qry_entered=request.POST.get('query')
        #print(qry_entered)
        return render(request,'search.html',{'dict':qry_entered,'wikipedia_result':scrape_wikipedia(qry_entered)})
        #{'dict':qry_entered,'search_results_key':scrape_function(qry_entered)})    
    else:
        return render(request,'search.html')


def developers(request):
    return render(request,'developers.html')

#wikipedia scrape begins
def scrape_wikipedia(qry):
    import wikipedia

    list_returned=wikipedia.search("what the hell is this python")  #return a list
    #print(list_returned[0])
    #print(wikipedia.summary(list_returned[0]))
    return wikipedia.summary(list_returned[0])

#wikipedia scrape ends
