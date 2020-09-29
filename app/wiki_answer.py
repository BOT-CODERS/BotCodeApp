# wikipedia scrape begins
def scrape_wikipedia(qry):
    import wikipedia

    list_returned = wikipedia.search(qry)  # return a list
    # print(list_returned[0])
    # print(wikipedia.summary(list_returned[0]))
    return wikipedia.summary(list_returned[0])