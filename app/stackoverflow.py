import requests
from bs4 import BeautifulSoup


# stackoverflow scrape begins
headers = dict()
headers[
    "User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"

def get_ques_text_and_link(q):
    res = requests.get("https://stackoverflow.com/search?q=" + q,
                       headers=headers)  # this is exactly the url when we search a question on stack overflow
    soup = BeautifulSoup(res.text, "html.parser")

    questions_data = {
        "questions": []
    }

    question = soup.select_one(".question-summary")
    q = question.select_one('.question-hyperlink')
    link = "https://stackoverflow.com" + q["href"]
    ques_text = q.getText()
    # print(ques_text)
    # print(link)
    return ques_text, link


def get_answer(url):
    # content = urllib.request.urlopen(url)
    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, features='lxml')
    try:
        accepted_content = soup.find_all('div', class_="js-post-body")

        return accepted_content[0].text.strip(), accepted_content[1].text.strip()

    except Exception as error:
        print(str(error))
        return None, 'not answered'



def stackoverflow(query):
    ques_text, link = get_ques_text_and_link(query)
    stackoverflow_list = ["question is : " + ques_text, "For Details visit : " + link]
    detailed_ques, answer = get_answer(link)
    if (detailed_ques is None):
        return ['The question is not answered in stackoverflow']
    stackoverflow_list.append("Detailed Question : " + detailed_ques)
    stackoverflow_list.append("Answer is : " + answer)
    return stackoverflow_list