# Web Scrapper Summary 

## Do your research and get useful links with one click!

### Project Explanation

This is a study project that aims to learn about web scrapping with Python code. 
Project functionalities: Desktop simple GUI that allow user to input the research subject. After input is filled, user opens the summary about the subject. The program scraps wikipedia and google scholar to find a summary about the subject and useful links for the user to dive into the search. 

### Developing Stack

This project is developed with Python, using PyQt5 for GUI building and BeautifulSoup for scrapping.
It also is my first implementation of MVCs architecture, using a model, controller and view (GUI).

### How can I use it?

Clone this repo in your local environment. Create a virtual environment with `python -m venv venv` or `python3 -m venv venv` and activate it with `venv\Scripts\activate` or `source venv/bin/activate`.

After cloning and creating a venv, install requirements with `pip install -r requirements.txt`.

For running it, simply run `python3 init.py` or `python init.py`.