# ScrapingTask

A web scraping application using the Scrapy Framework to extract the newest 20 articles on https://nbs.sk/en/ and an API to display the data that was scraped using the FastAPI framework and SQLalchemy.

To Start the application you first need to access the virtual environment by typing "env\Scripts\activate.ps1" in the terminal while inside the main directory.
After that you can start the crawler by using the powershell("./runCrawler") or shell/bash script("sh runCrawler.sh | bash runCrawler.sh").
The FastAPI application can be started in a similar way by using powershell("./runApi") or shell/bash("sh runApi.sh | bash runApi.sh").

The API has only 3 types of requests that can be send:

GET: /articles - which gives you all the articles in the database.

GET: /articles/id - which gives you a specific article.

DELETE: /articles/id - which delets a specific article.
