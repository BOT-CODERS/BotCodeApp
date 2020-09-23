from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from . import wiki_answer as wiki

def general_answer(q, PATH):
    url = f'https://duckduckgo.com/?q={q.lower().replace(" ", "+")}&ia=web'
    # print(url)
    options = Options()
    options.headless = True

    try:
        driver = webdriver.Chrome(executable_path=PATH, options=options)
    except:
        message = "OOPS! Our SEO suggests searching this query in other options! \n THANK YOU! :)"
        return message

    driver.get(url)

    # prettify the source code and save in source_code
    # soup = BeautifulSoup(driver.page_source, 'html.parser')
    # source_code = soup.prettify()

    # get information if card is present
    try:
        less_btn = driver.find_element_by_class_name("module__toggle--more")
        less_btn.click()
        result_elements = driver.find_elements_by_class_name(
            "module__text")  # use "module__content to get the full card text"
        text = [i.text for i in result_elements]
        # print(*text, sep='\n')
        return str(*text)

    except:
        pass

    # if card is not present then collect the short summary provided by the site
    try:

        result_elements = driver.find_elements_by_class_name("result__snippet")
        snippets = [i.text for i in result_elements[:5]]
        # print(*snippets, sep='\n')
        return snippets
        
    except Exception as e:
        # print(f"Result Error: {e}")
        pass

# general_answer scrape ends
