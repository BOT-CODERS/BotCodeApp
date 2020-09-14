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