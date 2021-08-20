#multiple search options (list), auto buy

import requests
import re
from selenium import webdriver
import sys

results = re.compile('"total_results":(\d*)')

listofsearch = []
allitems = {}

def total():
    print('clearance:', results.search(requests.get('https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v1?key=ff457966e64d5e877fdbad070f276d18ecec4a01&category=5q0ga&channel=WEB&count=24&default_purchasability_filter=true&include_sponsored=true&offset=0&page=%2Fc%2F5q0ga&platform=desktop&pricing_store_id=1336&scheduled_delivery_store_id=1336&store_ids=1336%2C1975%2C3375%2C955%2C2139&visitor_id=017929D48C04020189016448C858D2EC').text).group(1))

def search(result):
    listofsearch.append(result)
    print(list(set(listofsearch)))
    done = input("(add/exit) ")
    if done == "add":
        search(input("search: "))
    elif done == "exit":
        return
    else:
        find(list(set(listofsearch)))

def find(los):
    print("Searching..")
    try:
        page = 0
        while not re.search("errors", requests.get('https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v1?key=ff457966e64d5e877fdbad070f276d18ecec4a01&category=5q0ga&channel=WEB&count=24&default_purchasability_filter=true&include_sponsored=true&offset={}&page=%2Fc%2F5q0ga&platform=desktop&pricing_store_id=1336&scheduled_delivery_store_id=1336&store_ids=1336%2C1975%2C3375%2C955%2C2139&visitor_id=017929D48C04020189016448C858D2EC'.format(str(page*24))).text):
            clearance = requests.get('https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v1?key=ff457966e64d5e877fdbad070f276d18ecec4a01&category=5q0ga&channel=WEB&count=24&default_purchasability_filter=true&include_sponsored=true&offset={}&page=%2Fc%2F5q0ga&platform=desktop&pricing_store_id=1336&scheduled_delivery_store_id=1336&store_ids=1336%2C1975%2C3375%2C955%2C2139&visitor_id=017929D48C04020189016448C858D2EC'.format(str(page*24))).json()
            try:
                items = 0
                while items < len(clearance["data"]["search"]["products"]):
                    for i in listofsearch:
                        if i in str(clearance["data"]["search"]["products"][items]["item"]["product_description"]["title"]).lower():
                            ## fix keyerror, maybe nonexisiant comparsion price, and tuple range out of index, while loops maybe causing problem? interruptions first few pages, maybe whileloop+requests
                            allitems["({}) price: {}, comparison: {}".format(clearance["data"]["search"]["products"][items]["item"]["product_description"]["title"], clearance["data"]["search"]["products"][items]["price"]["formatted_current_price"], clearance["data"]["search"]["products"][items]["price"]["formatted_comparison_price"])] = clearance["data"]["search"]["products"][items]["item"]["enrichment"]["buy_url"]
                    items += 1
            except Exception as e:
                print(e)
            finally:
                page += 1
                print(page)
    except Exception as e:
        print(e)
    else:
        print(allitems)
        buy(input("Buy: "))

def buy(i):
    try:
        autobuy(allitems[i])
    except:
        print("could not buy..")
    finally:
        tryagain = input("(exit) or continue? ")
        if tryagain == "exit":
            return
        else:
            print(allitems)
            buy(input("Buy: "))

def autobuy(item):
    #fix
    clearance = requests.get(item)
    print(clearance)
    
    #browser = webdriver.Chrome()
    #browser.get("https://www.target.com/c/clearance/-/N-5q0ga?lnk=dNav_clearance")
    

def terminal(CMD):
    if CMD == "total":
        total()
    elif CMD == "buy":
        listofsearch.clear()
        allitems.clear()
        search(input("search: "))



while True:
    terminal(input("CMD: "))




