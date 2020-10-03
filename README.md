# **BOT CODE**

![GIF](https://github.com/BOT-CODERS/BotCodeApp/blob/master/Bot_Code_Demo.gif)

>## ✍&nbsp; PROJECT DESCRIPTION
A bot that automates solving a task on a website.We will simply create a Bot which searches solution on Google and provides the best solution on the Platform. This can be also used to solve errors. So we can provide a platform where users can post their problems and the algorithm which scraps the details and finds the solution from the internet and displays it on the screen.

>## 📂&nbsp; RELEVANT TECHNOLOGY
Any web technology can be used but I am thinking about using NodeJS ecosystem.

* Django
* Web Scrapping
* NLP


>## 💻&nbsp; GETTING STARTED

=> **Fork <a href=https://github.com/LetsUpgrade/BOT-CODE><img src="https://img.icons8.com/ios/24/000000/code-fork.png"></a>this repository to start contributing.**

=> Open your Git Bash command window and in the root directory type the following commands :
```bash
    1) git init -initializes the git repository from the GitHub. 
    2) git clone -Clone the repository to your local machine
      (git clone https://github.com/<your-github-username>/LetsUpgrade/BOT-CODE)
```    

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

