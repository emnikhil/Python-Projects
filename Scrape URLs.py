from bs4 import BeautifulSoup
import requests

#creat empty list
urls = []

def scrape(site):
    #get the request from url
    r = requests.get(site)
    #convert the text
    s = BeautifulSoup(r.text, "html.parser")
    for i in s.find_all("a"):
        href = i.attrs['href']
        if href.startswith("/"):
            site = site + href
            if site not in urls:
                urls.append(site)
                print(site)
                #calling the scrape function itself
                scrape(site)

#main function

if __name__ == "__main__":
    #website to be scrape
    site = "https://www.google.com//"
    #calling function
    scrape(site)