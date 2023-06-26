import json

import requests
from bs4 import BeautifulSoup
from pprint import pprint


def extract_links(url, element, class_name, link_attr='href', base_url=''):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    titles = soup.find_all(element, class_=class_name)

    links = []
    for title in titles[:3]:
        url_link = title.find('a')
        if url_link:
            link = url_link.get(link_attr)
            if link:
                res_link = f"{base_url}{link}"
                links.append(res_link)

    return links


def get_data():
    url1 = "https://www.redcrescent.kg/ru/press-center/events/"
    url2 = "https://www.unicef-irc.org/events/"
    url3 = "https://www.giz.de/en/worldwide/99887.html"
    url4 = "https://soros.kg/category/contests/"
    new_dict = {}
    links1 = extract_links(url1, 'p', 't-1 my-2 t-title с-text-primary l-inherit l-hover-primary l-hover-underline-none transition', base_url='https://www.redcrescent.kg')
    for link in links1:
        key = link.split('/')[-2]
        new_dict[key] = {
            "url": link
        }

    links2 = extract_links(url2, 'div', 'storyBoxReadmore', link_attr='href', base_url='https://www.unicef-irc.org/events/')
    for link in links2:
        key = link.split('/')[-1].split('.')[0]
        new_dict[key] = {
            "url": link
        }

    links3 = extract_links(url3, 'section', 'newEvent', base_url='https://www.giz.de')
    for link in links3:
        key = link.split('/')[-1].split('.')[0]
        new_dict[key] = {
            "url": link
        }

    links4 = extract_links(url4, 'div', 'fusion-rollover-content')
    if len(links4) > 0:
        for link in links4:
            key = link.split('/')[-2]
            new_dict[key] = {
                "url": link
            }
    else:
        print("No links found in url4.")

    with open("events.json", "w") as file:
        json.dump(new_dict, file, indent=4, ensure_ascii=False)


def check_news_update():
    with open("events.json") as file:
        new_dict = json.load(file)

    url1 = "https://www.redcrescent.kg/ru/press-center/events/"
    url2 = "https://www.unicef-irc.org/events/"
    url3 = "https://www.giz.de/en/worldwide/99887.html"
    url4 = "https://soros.kg/category/contests/"
    fresh_news = {}
    links1 = extract_links(url1, 'p','t-1 my-2 t-title с-text-primary l-inherit l-hover-primary l-hover-underline-none transition', base_url='https://www.redcrescent.kg')
    for link in links1:
        key = link.split('/')[-2]
        if key in new_dict:
            continue
        else:
            new_dict[key] = {
                "url": link
            }

            fresh_news[key] = {
                "url": link
            }

    links2 = extract_links(url2, 'div', 'storyBoxReadmore', link_attr='href', base_url='https://www.unicef-irc.org/events/')
    for link in links2:
        key = link.split('/')[-1].split('.')[0]
        if key in new_dict:
            continue
        else:
            new_dict[key] = {
                "url": link
            }

            fresh_news[key] = {
                "url": link
            }

    links3 = extract_links(url3, 'section', 'newEvent', base_url='https://www.giz.de')
    for link in links3:
        key = link.split('/')[-1].split('.')[0]
        if key in new_dict:
            continue
        else:
            new_dict[key] = {
                "url": link
            }

            fresh_news[key] = {
                "url": link
            }

    links4 = extract_links(url4, 'div', 'fusion-rollover-content')
    if len(links4) > 0:
        for link in links4:
            key = link.split('/')[-2]
            if key in new_dict:
                continue
            else:
                new_dict[key] = {
                    "url": link
                }

                fresh_news[key] = {
                    "url": link
                }
    else:
        print("No links found in url4.")

    with open("events.json", "w") as file:
        json.dump(new_dict, file, indent=4, ensure_ascii=False)

    return fresh_news