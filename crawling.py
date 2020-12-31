import requests, json
from bs4 import BeautifulSoup

domain = web_url
data = []
for i in range(112):
    page = requests.get(domain + '/?pageid='+ str(i + 1) +'&page_id=33').content
    soup = BeautifulSoup(page, 'html.parser')
    links = soup.select("td > div > a")
    uids = soup.select("td.kboard-list-uid")
    kokomong = soup.select("td.kboard-list-view")
    for seq,link in enumerate(links):
        url = domain+link.attrs['href']
        t_uid = url.split('&')[2].split('=')[1]
        t_postnum = uids[seq+1].text
        t_postname = links[seq].text.strip()
        t_kokomong = kokomong[seq+1].text
        tmp = {'uid' : t_uid,
               'postnum' : t_postnum,
               'postname' : t_postname,
               'kokomong' : t_kokomong}
        data.append(tmp)

for i,k in enumerate(data):
    print(k)


with open('C://Users//hhhhh//PycharmProjects//log_parser/url-20-05-31.json','w',encoding='utf-8') as test_data:
    for i in range(len(data)):
        json.dump(data[i],test_data, ensure_ascii = False)
        test_data.write('\n')
