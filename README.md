# BotCodeApp

### A smart search engine to summarize big content obtained from web pages

## HOW TO RUN THE BOT?

- Make a virtual environment using
```
virtualenv <env. name> 
```
  Example: ``` virtualenv venv```
  
 - Activate the environment:
 ```
 source <env.name>/bin/activate
 ```

- Run the following command to install the dependencies:
```
pip install -r requirements.txt
```

- Now, download the chromedriver, based on your Google Chrome version, and add it to the root directory.

- Copy the path of this driver, and open app/views.py and look for a variable named:
```
Driver_Path
```

- Replace the string assigned to that variable, with the path of your driver.
  
  Example:
```
Driver_Path = 'BotCodeApp/chromedriver'
```

- Go back to Terminal/Command Prompt, and type in the following command to run the project.
```
python manage.py runserver
```

# :sparkles: HURRAY! YOU ARE NOW A BOTCODE USER! :) 
