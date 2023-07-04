import json

import requests
from bs4 import BeautifulSoup
from pprint import pprint


def extract_links(url, element, class_name, link_attr='href', base_url='', tag='', else_class='', tag_div=''):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    titles = soup.find_all(element, class_=class_name)

    links = []
    for title in titles[:3]:
        if else_class:
            check_tag = title.find("div", {"class": tag_div})
            check_tag_span = check_tag.find("span").text.strip()
            if check_tag_span == tag:
                url_div = title.find("div", {"class": else_class})
                url_link = url_div.find("a")
                if url_link:
                    link = url_link.get(link_attr)
                    if link:
                        res_link = f"{base_url}{link}"
                        links.append(res_link)
        else:
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
    url5 = "https://soros.kg/category/grants/"
    new_dict = {}
    links1 = extract_links(url1, 'p', 't-1 my-2 t-title с-text-primary l-inherit l-hover-primary l-hover-underline-none transition', base_url='https://www.redcrescent.kg')
    for link in links1:
        key = link.split('/')[-2]
        new_dict[key] = {
            "url": link
        }

    links2 = extract_links(url2, 'div', 'storyBox', link_attr='href', base_url='https://www.unicef-irc.org/events/', tag='Grant', else_class='storyBoxReadmore', tag_div='storyBoxType')
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


    links5 = extract_links(url5, 'div', 'fusion-rollover-content')
    if len(links5) > 0:
        for link in links5:
            key = link.split('/')[-2]
            new_dict[key] = {
                "url": link
            }
    else:
        print("No links found in url5.")

    with open("events.json", "w") as file:
        json.dump(new_dict, file, indent=5, ensure_ascii=False)


def check_news_update():
    with open("events.json") as file:
        new_dict = json.load(file)

    # url1 = "https://www.redcrescent.kg/ru/press-center/events/"
    url2 = "https://www.unicef-irc.org/events/"
    # url3 = "https://www.giz.de/en/worldwide/99887.html"
    url4 = "https://soros.kg/category/contests/"
    url5 = "https://soros.kg/category/grants/"
    fresh_news = {}
    # links1 = extract_links(url1, 'p','t-1 my-2 t-title с-text-primary l-inherit l-hover-primary l-hover-underline-none transition', base_url='https://www.redcrescent.kg')
    # for link in links1:
    #     key = link.split('/')[-2]
    #     if key in new_dict:
    #         continue
    #     else:
    #         new_dict[key] = {
    #             "url": link
    #         }

    #         fresh_news[key] = {
    #             "url": link
    #         }

    links2 = extract_links(url2, 'div', 'storyBox', link_attr='href', base_url='https://www.unicef-irc.org/events/', tag='Grant', else_class='storyBoxReadmore', tag_div='storyBoxType')
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

    # links3 = extract_links(url3, 'section', 'newEvent', base_url='https://www.giz.de')
    # for link in links3:
    #     key = link.split('/')[-1].split('.')[0]
    #     if key in new_dict:
    #         continue
    #     else:
    #         new_dict[key] = {
    #             "url": link
    #         }

    #         fresh_news[key] = {
    #             "url": link
    #         }

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

    links5 = extract_links(url5, 'div', 'fusion-rollover-content')
    if len(links5) > 0:
        for link in links5:
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
        print("No links found in url5.")

    with open("events.json", "w") as file:
        json.dump(new_dict, file, indent=5, ensure_ascii=False)

    return fresh_news