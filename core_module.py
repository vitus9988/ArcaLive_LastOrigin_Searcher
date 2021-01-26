from bs4 import BeautifulSoup
import requests
import urllib.request
from tqdm import tqdm
import os
from moviepy.editor import *


def wc(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    return soup


def NamuliveSearch(radiovalue, keyword):
    global soup, mode
    mode = ''


    if radiovalue == 0:
        soup = wc(url='https://arca.live/b/lastorigin?{}category=공략&target=title_content&keyword={}'.format(mode,keyword))
    elif radiovalue == 1:
        soup = wc(url='https://arca.live/b/lastorigin?{}category=공략&target=title&keyword={}'.format(mode,keyword))

    detail = soup.find_all('a','vrow')
    base_url = 'https://arca.live'
    detail_arr = []
    for i in detail:
        try:
            link = i.get('href')
            title = i.find('span','title').text.strip()
            detail_arr.append(title)
            detail_arr.append(base_url+link)
        except:
            continue
    return detail_arr


def RuliwebSearch(keyword):
    soup = wc(url='https://bbs.ruliweb.com/mobile/game/84992?search_type=subject_content&search_key={}&cate=4'.format(keyword))
    detail = soup.find_all('tr','table_body')
    detail_arr = []
    for i in detail:
        try:
            title = i.find('div','relative').find('a').text.strip()
            link = i.find('div','relative').find('a').get('href')
            detail_arr.append(title)
            detail_arr.append(link)
        except:
            continue
    return detail_arr


def NavercafeSearch(keyword):
    pass



# def img_download(img_path, page_count):
#
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}
#     page = 1
#
#     while True:
#         soup = wc(url='https://arca.live/b/lastorigin?category=%EC%95%BC%EC%A7%A4&p={}'.format(page))
#         detail = soup.find_all('a', 'vrow')
#         base_url = 'https://arca.live'
#
#         for i in detail:
#             try:
#                 text_num = i.find('span', 'vcol col-id').text.strip()
#                 link = i.get('href')
#                 title = i.find('span', 'title').text.strip()
#                 img_url = base_url + link
#                 yazzl_list = image_link(img_url)
#
#                 if len(yazzl_list) != 0:
#                     count = 1
#                     if os.path.exists(img_path+'/{}+{}'.format(text_num, title)):
#                         pass
#                     os.makedirs(img_path+'/{}+{}'.format(text_num, title))
#
#                     for k in yazzl_list:
#                         request_ = urllib.request.Request(k, None, headers)
#                         response = urllib.request.urlopen(request_)
#                         f = open('{}/{}+{}/{}.png'.format(img_path,text_num,title,count),'wb')
#                         #f = open('{}/{}+{}.png'.format(img_path, count), 'wb')
#                         f.write(response.read())
#                         f.close()
#                         count += 1
#                 else:
#                     pass
#             except:
#                 continue
#         page += 1
#
#         if page > page_count:
#             break


def created_img_download(img_path, page_count):

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}
    page = 1

    while True:
        soup = wc(url='https://arca.live/b/lastorigin?category=%EC%95%BC%EC%A7%A4&target=all&keyword=&p={}'.format(page))
        detail = soup.find_all('a', 'vrow')
        base_url = 'https://arca.live'

        for i in detail:
            try:
                text_num = i.find('span', 'vcol col-id').text.strip()
                link = i.get('href')
                title = i.find('span', 'title').text.strip()
                img_url = base_url + link
                yazzl_list = gif_img_link(img_url)

                if len(yazzl_list) != 0:
                    count = 1
                    if os.path.exists(img_path+'/{}+{}'.format(text_num, title)):
                        pass
                    os.makedirs(img_path+'/{}+{}'.format(text_num, title))

                    for k in yazzl_list:
                        request_ = urllib.request.Request(k, None, headers)
                        response = urllib.request.urlopen(request_)
                        if k[-3:] == 'mp4':
                            f = open('{}/{}+{}/{}.mp4'.format(img_path, text_num, title, count), 'wb')
                            f.write(response.read())
                            f.close()
                            clip = (VideoFileClip('{}/{}+{}/{}.mp4'.format(img_path, text_num, title, count)))
                            clip.write_gif('{}/{}+{}/{}.gif'.format(img_path, text_num, title, count))

                        else:
                            f = open('{}/{}+{}/{}.png'.format(img_path, text_num, title, count), 'wb')
                            f.write(response.read())
                            f.close()
                        count += 1
                else:
                    pass
            except:
                continue
        page += 1

        if page > page_count:
            break



def image_link(borad_link):
    soup = wc(url=borad_link)
    stat = soup.find('div','fr-view article-content')
    detail = stat.find_all('img')
    result = ['https:' + i.get('src') for i in detail]
    if len(result) == 0:
        pass
    return result


def gif_img_link(img_link):
    soup = wc(url=img_link)
    stat = soup.find('div', 'fr-view article-content')
    detail = stat.find_all('img')
    result = ['https:' + i.get('src') for i in detail]
    if len(detail) == 0:
        gif_detail = stat.find_all('video')
        result = ['https:' + i.get('src') for i in gif_detail]
        return result
    return result




if __name__ == '__main__':
    board_image_link('C:\yazzal_test')