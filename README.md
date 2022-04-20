# GameWebscraper
This steam webscrapper was a project created after freshmen year in college. I was introduced to the library BeautifulSoup, that is used for webscrapping data offline, and was able to understand how given an html layout, how to select data off that website, and potentially use it for comparative purposes.

# Running the Project
In order to run the project, some libraries may have to be impoorted, including BeautifulSoup, pandas, requests, and time.

# Project Functionalities
More specifically, this webscrapper uses the latest html layout of a steam website which includes the prices, and current discounts of the games currently on the page. Each page only holds 50 games worth of data. Thus, by splitting the html layout appropriately, I was able to get the title, the price, and the discount price, and print out the information for the the top 200 games on steam. Not all results will be printed, and thus I create a csv file to store all that information in.

![image](https://user-images.githubusercontent.com/89613119/164303841-5eedfa42-f36e-48c9-b48a-7423c48ac35c.png)
