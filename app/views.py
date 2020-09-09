from django.shortcuts import render
import nltk
from .models import Destination #importing class from models
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

    return render(request,'home.html')  #passing object dynamically 
def add(request):
    query=request.POST['query']
    query=query.upper()
    res=get_continuous_chunks(query)
    dest1=Destination()
    dest1.name="Java"  #keeping the name of class variable
    dest1.desc="This is Java"
    dest2=Destination()
    dest2.name="Python"  #keeping the name of class variable
    dest2.desc="This is python"
    dests=[dest1,dest2]  #creating list of objects
    
    return render(request,"result.html",{"result":res,'dests':dests})