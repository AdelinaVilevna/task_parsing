import csv
import datetime
import requests
from bs4 import BeautifulSoup

main_url = 'https://www.kivano.kg/mobilnye-telefony'

def get_html(url):
    res = requests.get(url)
    return res.text

def get_all_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    all_page = soup.find('div', class_ = 'list-view').find_all('div', class_ = 'item product_listbox')
    print(all_page)

    for page in all_page:
        try:
            title = page.find('div', class_ = 'listbox_title').find('a').get('href')
            title_main = 'https://www.kivano.kg' + title
        except:
            title_main = ''
        try:
            price = page.find('div', class_ = 'listbox_price').get('strong')
        except:
            price = ''
        try:
            img = page.find('div', class_ = 'listbox_img').get('img')
            img_full = 'https://www.kivano.kg' + img   
        except:
            img_full = ''
        
        data = {'title': title_mainl, 'price': price, 'image': img_full }
        return(data)


def write_csv(data):
    with open('kivano.csv', 'a') as file:
        writer = csv.writer(file)
        write.writerow([data['title'], data['price'], data['image']])
        print([data['title'], data['price'], data['image']], 'parsed')
        


def main():
    html = get_html(main_url)
    data_page = get_all_page(html)
    html_text = get_html(main_url)
    write_csv(data)
    print(data)

if __name__ == '__main__':        
    main()
