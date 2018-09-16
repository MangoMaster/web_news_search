# web_news_search

web individual project: news search
author: Wei JiaDong. All rights reserverd.

## dependencies

Python3 3.6.6  
Django 2.1.1  
Requests 2.19.1  
Beautifulsoup4 4.6.3  
Jieba 0.39  

## install

First, install python3.  
Then, install other dependencies through pip3:  
```bash
pip3 install --upgrade Django Requests Beautifulsoup4 Jieba
```
You may have to add option "--user" at the back or add "sudo" at the front.  

## run

under src directory, perform:  
```bash
python3 ./manage.py runserver
```
to run the web server.  

under src directory, perform:  
```bash
python3 ./manage.py createsuperuser
```
and follow the steps to create an admin to the web server.

## use

* search
    * Type "localhost:8000/search" in the address bar of your web browser to enter the main page of Penguin News Search.
    * Type something you are interested in in the search bar.
    * Click "Search" button to search news in Penguin News Search
    * Click "下一页" or "上一页" to see all the results.
* admin
    * Type "localhost:8000/admin" in the address bar of your web browser to enter the admin page of Django.
    * Type in your admin username and password to log in.
    * Manage the news & indexes in your database.

## license

MIT license.

## software design document

Click here: [software design document](./docs/software_design_document.md).