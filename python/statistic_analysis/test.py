# from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#html = urlopen("https://sports.daum.net/team/epl")  

base_url = "https://sports.daum.net"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)

epl = "/team/epl"
driver.get(base_url+epl)
bsObject = BeautifulSoup(driver.page_source, 'html.parser')
# base_url = "https://sport.daum.net"
# bsObject = BeautifulSoup(html, "html.parser") 

team_name = []
team_player_link = []
team_schedule_link = []
team_record_link = []

for team in bsObject.find_all(attrs={'class':'cont_item'}):
    #print(cover)
    # print(cover.find('strong').text) #Team Name
    # print(cover.find('a',text='일정').get('href'))
    # print(cover.find('a',text='선수').get('href'))
    # print(cover.find('a',text='기록').get('href'))
   
    team_name.append(team.find('strong').text)
    team_schedule_link.append(team.find('a',text='일정').get('href'))
    team_player_link.append(team.find('a',text='선수').get('href'))
    team_record_link.append(team.find('a',text='기록').get('href'))

for player in team_player_link :
    # new_url = base_url + player[7:]
    # print(new_url)
    # temp_html = urlopen(new_url)
    # meta_data = BeautifulSoup(temp_html, "html.parser") 
    # print(meta_data)
    driver.get(base_url + player[7:])
    meta_data = BeautifulSoup(driver.page_source, 'html.parser')
    # team_list = meta_data.find(attrs={'class':'menuComponent section_teamplayer'})
    forward = meta_data.find(attrs={'data-position-code':'FW'})
    midfilder = meta_data.find(attrs={'data-position-code':'MF'})
    defender = meta_data.find(attrs={'data-position-code':'DF'})
    goalkeeper = meta_data.find(attrs={'data-position-code':'GK'})
    
    for player in forward.find_all('li') :
        print(player.find('strong').text) #선수이름

#    for player in forward.find_all('li') :
#         print(player.find('strong').text)
    
    # print(meta_data)
    # print(cover.find(attrs={'class':'tit_thumb'}))
# for meta in bsObject.head.find_all('meta'):
#     print(meta.get('content'))
#     html = urlopen(book_page_url)
#     bsObject = BeautifulSoup(html, "html.parser")
#     title = bsObject.find('meta', {'property':'rb:itemName'}).get('content')
#     author = bsObject.select('span.name a')[0].text
#     image = bsObject.find('meta', {'property':'rb:itemImage'}).get('content')
#     url = bsObject.find('meta', {'property':'rb:itemUrl'}).get('content')
#     originalPrice = bsObject.find('meta', {'property': 'rb:originalPrice'}).get('content')
#     salePrice = bsObject.find('meta', {'property':'rb:salePrice'}).get('content')
#     print(index+1, title, author, image, url, originalPrice, salePrice)