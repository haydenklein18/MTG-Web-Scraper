import urllib

import certifi
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient
import time
from bisect import bisect_left
import bisect

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return True
    else:
        return False


def checkLegendary(text):
    if text.contains(" "):
        split = text.split("-")
        before_hyphen = split[0]
        after_hyphen = split[1]
        split2 = before_hyphen.split(" ")
        if split2[0] != "Legnedary":
            split2(0, "")
        return split2[0], split2[1], after_hyphen[0]
    else:
        return "", text, ""


def scrape():
    count = 0
    total_seconds = 0
    mongo_client = load_into_mongodb()
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(executable_path="C:/Users/hayde/Downloads/chromedriver.exe", options=options)
    URL = "https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&name=|[a]|[b]|[c]|[d]|[e]|[f]|[g]|[h]|[i]|[j]|[k]|[l]|[m]|[n]|[o]|[p]|[q]|[r]|[s]|[t]|[u]|[v]|[w]|[x]|[y]|[z] "
    driver.get(URL)
    win_list = driver.window_handles
    driver.switch_to.window(win_list[-1])
    name_list = []
    try:
        link = driver.find_element_by_id("wizardCookieBannerOptIn")
        link.click()
    except:
        None
    for f in range(1, 269):
        for x in range(100):
            # privacy_button = driver.find_element_by_class_name("close-me")
            # privacy_button.click()
            start = time.time()
            if x < 10:
                x = "0" + str(x)

            link = driver.find_element_by_id(
                "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl00_listRepeater_ctl" + str(
                    x) + "_cardTitle")
            link.click()
            link = driver.find_element_by_id("cardTextSwitchLink2")
            link.click()
            win_list = driver.window_handles
            driver.switch_to.window(win_list[-1])
            dual_card_bool = existsElement("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl02_cardImage",
                                           driver)
            modal_card_bool = existsElement("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl04_cardImage",
                                            driver)

            if dual_card_bool:
                card1_name = ""
                mana1 = ""
                cmc1 = -1
                card1_super_type = ""
                card1_main_type = ""
                card1_sub_type = ""
                card1_text = ""
                flavor1_text = ""
                set1 = ""
                other1_sets = ""
                rarity1 = ""
                card1_number = -1
                artist1 = ""
                community1_rating = -1.0
                number1_of_voters = -1
                card2_name = ""
                mana2 = ""
                cmc2 = -1
                card2_super_type = ""
                card2_main_type = ""
                card2_sub_type = ""
                card2_text = ""
                flavor2_text = ""
                set2 = ""
                other2_sets = ""
                rarity2 = ""
                card2_number = -1
                artist2 = ""
                community2_rating = -1.0
                number2_of_voters = -1

                try:
                    name_ele = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl02_nameRow")
                    name = name_ele.find_element_by_class_name("value")
                    name = name.text
                    name = name.replace("\"", "")
                    card1_name = name
                    name_ele = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_nameRow")
                    name = name_ele.find_element_by_class_name("value")
                    name = name.text
                    name = name.replace("\"", "")
                    card2_name = name

                except:
                    None

                try:
                    big_mana = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl02_manaRow")
                    mana_ele = big_mana.find_element_by_class_name("value")
                    mana_list = mana_ele.find_elements_by_tag_name("img")
                    for z in mana_list:
                        mana1 += z.get_attribute("alt") + " "
                    big_mana = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_manaRow")
                    mana_ele = big_mana.find_element_by_class_name("value")
                    mana_list = mana_ele.find_elements_by_tag_name("img")
                    for z in mana_list:
                        mana2 += z.get_attribute("alt") + " "
                except:
                    None

                try:
                    cmc = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl02_cmcRow")
                    cmc_ele = cmc.find_element_by_class_name("value")
                    cmc1 = int(cmc_ele.text)

                    cmc = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_cmcRow")
                    cmc_ele = cmc.find_element_by_class_name("value")
                    cmc1 = int(cmc_ele.text)
                except:
                    None

                try:
                    type = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl02_cmcRow")
                    type_ele = type.find_element_by_class_name("value")
                    card1_type = type_ele.text
                    results1 = checkLegendary(card1_type)
                    card1_super_type = results1[0]
                    card1_main_type = results1[1]
                    card1_sub_type = results1[2]

                    type = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_cmcRow")
                    type_ele = type.find_element_by_class_name("value")
                    card2_type = type_ele.text
                    results2 = checkLegendary(card2_type)
                    card2_super_type = results2[0]
                    card2_main_type = results2[1]
                    card2_super_type = results2[2]
                except:
                    None

                try:
                    card_text = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl02_textRow")
                    card_text_ele = card_text.find_element_by_class_name("value")
                    card_text_box0 = card_text_ele.find_elements_by_class_name("cardtextbox")
                    card_text_box = ""
                    for y in card_text_box0:
                        children = y.find_elements_by_xpath(".//*")
                        for x in children:
                            if isElement(x, "img"):
                                card_text_box += x.get_attribute("alt") + " "
                            elif isElement(x, "i"):
                                print("", end="")
                            else:
                                card_text_box += x.text + " "
                        card_text_box += y.text + " "
                    card1_text = card_text_box

                    card_text = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_textRow")
                    card_text_ele = card_text.find_element_by_class_name("value")
                    card_text_box0 = card_text_ele.find_elements_by_class_name("cardtextbox")
                    card_text_box = ""
                    for y in card_text_box0:
                        children = y.find_elements_by_xpath(".//*")
                        for x in children:
                            if isElement(x, "img"):
                                card_text_box += x.get_attribute("alt") + " "
                            elif isElement(x, "i"):
                                print("", end="")
                            else:
                                card_text_box += x.text + " "
                        card_text_box += y.text + " "
                    card2_text = card_text_box
                except:
                    None

                try:
                    flavor = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl02_FlavorText")
                    flavor_box = flavor.find_element_by_class_name("cardtextbox")
                    flavor1_text = flavor_box.text

                    flavor = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_FlavorText")
                    flavor_box = flavor.find_element_by_class_name("cardtextbox")
                    flavor1_text = flavor_box.text
                except:
                    None

                try:
                    set = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl02_currentSetSymbol")
                    set1 = set.text

                    set = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_currentSetSymbol")
                    set2 = set.text
                except:
                    None

                try:
                    other_sets0 = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl02_otherSetsRow")
                    sets_ele = other_sets0.find_elements_by_tag_name("img")
                    for p in sets_ele:
                        other1_sets += p.get_attribute("alt") + " , "

                    other_sets0 = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_otherSetsRow")
                    sets_ele = other_sets0.find_elements_by_tag_name("img")
                    for p in sets_ele:
                        other2_sets += p.get_attribute("alt") + " , "
                except:
                    None

                try:
                    rarity = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl02_rarityRow")
                    rarity_ele = rarity.find_element_by_class_name("value")
                    rarity_span = rarity_ele.find_elements_by_tag_name("span")
                    rarity1 = rarity_span[0].text

                    rarity = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_rarityRow")
                    rarity_ele = rarity.find_element_by_class_name("value")
                    rarity_span = rarity_ele.find_elements_by_tag_name("span")
                    rarity2 = rarity_span[0].text
                except:
                    None

                try:
                    card_num = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl02_numberRow")
                    card1_number = int(card_num.text)

                    card_num = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_numberRow")
                    card2_number = int(card_num.text)
                except:
                    None

                try:
                    artist = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl02_ArtistCredit")
                    artist_ele = artist.find_element_by_tag_name("a")
                    artist1 = artist_ele.text

                    artist = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_ArtistCredit")
                    artist_ele = artist.find_element_by_tag_name("a")
                    artist2 = artist_ele.text
                except:
                    None

                try:
                    rating = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl02_currentRating_textRating")
                    community1_rating = float(rating.text)

                    rating = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_currentRating_textRating")
                    community2_rating = float(rating.text)
                except:
                    None

                try:
                    raters = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl02_currentRating_totalVotes")
                    number1_of_voters = int(raters.text)

                    raters = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_currentRating_totalVotes")
                    number2_of_voters = int(raters.text)
                except:
                    None

                image1_url = driver.find_element_by_id(
                    "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl02_cardImage").get_attribute("src")

                image2_url = driver.find_element_by_id(
                    "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl02_cardImage").get_attribute("src")

                driver.execute_script("window.history.go(-2)")
                if not BinarySearch(name_list, card1_name):
                    add_to_mongodb(mongo_client, card1_name, mana1, cmc1, card1_super_type, card1_main_type,
                                   card1_sub_type, card1_text, flavor1_text, set1,
                                   other1_sets,
                                   rarity1,
                                   card1_number, artist1,
                                   community1_rating, number1_of_voters, image1_url)

                    bisect.insort(name_list, card1_name)
                if not BinarySearch(name_list, card2_name):
                    add_to_mongodb(mongo_client, card2_name, mana2, cmc2, card2_super_type, card2_main_type,
                                   card2_sub_type, card2_text, flavor2_text, set2,
                                   other2_sets,
                                   rarity2,
                                   card2_number, artist2,
                                   community2_rating, number2_of_voters, image2_url)
                    bisect.insort(name_list, card2_name)
                end = time.time()
                time_taken = end - start
                total_seconds = total_seconds + time_taken
                count = count + 1
                print("Added " + card1_name + " without issue, total time for scrape and entry: " + str(
                    time_taken / 2)
                      + " seconds. Total time elapsed: " + str(
                    total_seconds) + " seconds . This card is Number: " + str(count))
                count = count + 1
                print("Added " + card2_name + " without issue, total time for scrape and entry: " + str(
                    time_taken / 2)
                      + " seconds. Total time elapsed: " + str(
                    total_seconds) + " seconds . This card is Number: " + str(count))

            elif modal_card_bool:
                card1_name = ""
                mana1 = ""
                cmc1 = -1
                card1_super_type = ""
                card1_main_type = ""
                card1_sub_type = ""
                card1_text = ""
                flavor1_text = ""
                set1 = ""
                other1_sets = ""
                rarity1 = ""
                card1_number = -1
                artist1 = ""
                community1_rating = -1.0
                number1_of_voters = -1
                card2_name = ""
                mana2 = ""
                cmc2 = -1
                card2_super_type = ""
                card2_main_type = ""
                card2_sub_type = ""
                card2_text = ""
                flavor2_text = ""
                set2 = ""
                other2_sets = ""
                rarity2 = ""
                card2_number = -1
                artist2 = ""
                community2_rating = -1.0
                number2_of_voters = -1

                try:
                    name_ele = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_nameRow")
                    name = name_ele.find_element_by_class_name("value")
                    name = name.text
                    name = name.replace("\"", "")
                    card1_name = name
                    name_ele = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl04_nameRow")
                    name = name_ele.find_element_by_class_name("value")
                    name = name.text
                    name = name.replace("\"", "")
                    card2_name = name
                except:
                    None

                try:
                    big_mana = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_manaRow")
                    mana_ele = big_mana.find_element_by_class_name("value")
                    mana_list = mana_ele.find_elements_by_tag_name("img")
                    for z in mana_list:
                        mana1 += z.get_attribute("alt") + " "
                    big_mana = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl04_manaRow")
                    mana_ele = big_mana.find_element_by_class_name("value")
                    mana_list = mana_ele.find_elements_by_tag_name("img")
                    for z in mana_list:
                        mana2 += z.get_attribute("alt") + " "
                except:
                    None

                try:
                    cmc = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_cmcRow")
                    cmc_ele = cmc.find_element_by_class_name("value")
                    cmc1 = int(cmc_ele.text)

                    cmc = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl04_cmcRow")
                    cmc_ele = cmc.find_element_by_class_name("value")
                    cmc1 = int(cmc_ele.text)
                except:
                    None

                try:
                    type = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_cmcRow")
                    type_ele = type.find_element_by_class_name("value")
                    card1_type = type_ele.text
                    card1_results = checkLegendary(card1_type)
                    card1_super_type = card1_results[0]
                    card1_main_type = card1_results[1]
                    card1_sub_type = card1_results[2]

                    type = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl04_cmcRow")
                    type_ele = type.find_element_by_class_name("value")
                    card2_type = type_ele.text
                    card2_results = checkLegendary(card2_type)
                    card2_super_type = card2_results[0]
                    card2_main_type = card2_results[1]
                    card2_sub_type = card2_results[2]

                except:
                    None

                try:
                    card_text = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_textRow")
                    card_text_ele = card_text.find_element_by_class_name("value")
                    card_text_box0 = card_text_ele.find_elements_by_class_name("cardtextbox")
                    card_text_box = ""
                    for y in card_text_box0:
                        children = y.find_elements_by_xpath(".//*")
                        for x in children:
                            if isElement(x, "img"):
                                card_text_box += x.get_attribute("alt") + " "
                            elif isElement(x, "i"):
                                print("", end="")
                            else:
                                card_text_box += x.text + " "
                        card_text_box += y.text + " "
                    card1_text = card_text_box

                    card_text = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl04_textRow")
                    card_text_ele = card_text.find_element_by_class_name("value")
                    card_text_box0 = card_text_ele.find_elements_by_class_name("cardtextbox")
                    card_text_box = ""
                    for y in card_text_box0:
                        children = y.find_elements_by_xpath(".//*")
                        for x in children:
                            if isElement(x, "img"):
                                card_text_box += x.get_attribute("alt") + " "
                            elif isElement(x, "i"):
                                print("", end="")
                            else:
                                card_text_box += x.text + " "
                        card_text_box += y.text + " "
                    card2_text = card_text_box
                except:
                    None

                try:
                    flavor = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_FlavorText")
                    flavor_box = flavor.find_element_by_class_name("cardtextbox")
                    flavor1_text = flavor_box.text

                    flavor = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl04_FlavorText")
                    flavor_box = flavor.find_element_by_class_name("cardtextbox")
                    flavor1_text = flavor_box.text
                except:
                    None

                try:
                    set = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_currentSetSymbol")
                    set1 = set.text

                    set = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl04_currentSetSymbol")
                    set2 = set.text
                except:
                    None

                try:
                    other_sets0 = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_otherSetsRow")
                    sets_ele = other_sets0.find_elements_by_tag_name("img")
                    for p in sets_ele:
                        other1_sets += p.get_attribute("alt") + " , "

                    other_sets0 = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl04_otherSetsRow")
                    sets_ele = other_sets0.find_elements_by_tag_name("img")
                    for p in sets_ele:
                        other2_sets += p.get_attribute("alt") + " , "
                except:
                    None

                try:
                    rarity = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_rarityRow")
                    rarity_ele = rarity.find_element_by_class_name("value")
                    rarity_span = rarity_ele.find_elements_by_tag_name("span")
                    rarity1 = rarity_span[0].text

                    rarity = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl04_rarityRow")
                    rarity_ele = rarity.find_element_by_class_name("value")
                    rarity_span = rarity_ele.find_elements_by_tag_name("span")
                    rarity2 = rarity_span[0].text
                except:
                    None

                try:
                    card_num = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_numberRow")
                    card1_number = int(card_num.text)

                    card_num = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl04_numberRow")
                    card2_number = int(card_num.text)
                except:
                    None

                try:
                    artist = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_ArtistCredit")
                    artist_ele = artist.find_element_by_tag_name("a")
                    artist1 = artist_ele.text

                    artist = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl04_ArtistCredit")
                    artist_ele = artist.find_element_by_tag_name("a")
                    artist2 = artist_ele.text
                except:
                    None

                try:
                    rating = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_currentRating_textRating")
                    community1_rating = float(rating.text)

                    rating = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl04_currentRating_textRating")
                    community2_rating = float(rating.text)
                except:
                    None

                try:
                    raters = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_currentRating_totalVotes")
                    number1_of_voters = int(raters.text)

                    raters = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl04_currentRating_totalVotes")
                    number2_of_voters = int(raters.text)
                except:
                    None

                image1_url = driver.find_element_by_id(
                    "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_cardImage").get_attribute("src")

                image2_url = driver.find_element_by_id(
                    "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl04_cardImage").get_attribute("src")

                driver.execute_script("window.history.go(-2)")
                if not BinarySearch(name_list, card1_name):
                    add_to_mongodb(mongo_client, card1_name, mana1, cmc1, card1_super_type, card1_main_type,
                                   card1_sub_type, card1_text, flavor1_text, set1,
                                   other1_sets,
                                   rarity1,
                                   card1_number, artist1,
                                   community1_rating, number1_of_voters, image1_url)

                    bisect.insort(name_list, card1_name)
                if not BinarySearch(name_list, card2_name):
                    add_to_mongodb(mongo_client, card2_name, mana2, cmc2, card2_super_type, card2_main_type,
                                   card2_sub_type, card2_text, flavor2_text, set2,
                                   other2_sets,
                                   rarity2,
                                   card2_number, artist2,
                                   community2_rating, number2_of_voters, image2_url)
                    bisect.insort(name_list, card2_name)
                end = time.time()
                time_taken = end - start
                total_seconds = total_seconds + time_taken
                count = count + 1
                print("Added " + card1_name + " without issue, total time for scrape and entry: " + str(
                    time_taken / 2)
                      + " seconds. Total time elapsed: " + str(
                    total_seconds) + " seconds . This card is Number: " + str(count))
                count = count + 1
                print("Added " + card2_name + " without issue, total time for scrape and entry: " + str(
                    time_taken / 2)
                      + " seconds. Total time elapsed: " + str(
                    total_seconds) + " seconds . This card is Number: " + str(count))


            else:
                count = count + 1
                start = time.time()
                card_name = ""
                mana = ""
                cmc = -1
                super_type = ""
                main_type = ""
                sub_type = ""
                card_text = ""
                flavor_text = ""
                set = ""
                other_sets = ""
                rarity = ""
                card_number = -1
                artist = ""
                community_rating = -1.0
                number_of_voters = -1
                image_url = ""
                try:
                    name_ele = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContentHeader_subtitleDisplay")
                    name = name_ele.text
                    name = name.replace("\"", "")
                    card_name = name
                except:
                    None

                try:
                    big_mana = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_manaRow")
                    mana_ele = big_mana.find_element_by_class_name("value")
                    mana_list = mana_ele.find_elements_by_tag_name("img")
                    for z in mana_list:
                        mana += z.get_attribute("alt") + " "
                except:
                    None

                try:
                    cmc = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_cmcRow")
                    cmc_ele = cmc.find_element_by_class_name("value")
                    cmc = int(cmc_ele.text)
                except:
                    None

                try:
                    type = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_typeRow")
                    type_ele = type.find_element_by_class_name("value")
                    text = type_ele.text
                    results = checkLegendary(text)
                    super_type = results[0]
                    main_type = results[1]
                    sub_type = results[2]
                except:
                    None
                try:
                    card_text = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_textRow")
                    card_text_ele = card_text.find_element_by_class_name("value")
                    card_text_box0 = card_text_ele.find_elements_by_class_name("cardtextbox")
                    card_text_box = ""
                    for y in card_text_box0:
                        children = y.find_elements_by_xpath(".//*")
                        for x in children:
                            if isElement(x, "img"):
                                card_text_box += x.get_attribute("alt") + " "
                            elif isElement(x, "i"):
                                print("", end="")
                            else:
                                card_text_box += x.text + " "
                        card_text_box += y.text + " "
                    card_text = card_text_box
                except:
                    None

                try:
                    flavor = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_FlavorText")
                    flavor_box = flavor.find_element_by_class_name("flavortextbox")
                    flavor_text = flavor_box.text
                except:
                    None

                try:
                    set = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_currentSetSymbol")
                    set = set.text
                except:
                    None

                try:
                    other_sets0 = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_otherSetsValue")
                    sets_ele = other_sets0.find_elements_by_tag_name("img")
                    for p in sets_ele:
                        other_sets += p.get_attribute("alt") + " , "
                except:
                    None

                try:
                    rarity = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_rarityRow")
                    rarity_ele = rarity.find_element_by_class_name("value")
                    rarity_span = rarity_ele.find_elements_by_tag_name("span")
                    rarity = rarity_span[0].text
                except:
                    None

                try:
                    card_num = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_CardNumberValue")
                    card_number = int(card_num.text)
                except:
                    None

                try:
                    artist = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ArtistCredit")
                    artist_ele = artist.find_element_by_tag_name("a")
                    artist = artist_ele.text
                except:
                    None

                try:
                    rating = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_currentRating_textRating")
                    community_rating = float(rating.text)
                except:
                    None

                try:
                    raters = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_currentRating_totalVotes")
                    number_of_voters = int(raters.text)
                except:
                    None

                try:

                    image_url = driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_cardImage").get_attribute("src")
                except:
                    None

                driver.execute_script("window.history.go(-2)")
                if not BinarySearch(name_list, card_name):
                    add_to_mongodb(mongo_client, card_name, mana, cmc, super_type, main_type, sub_type, card_text,
                                   flavor_text, set,
                                   other_sets, rarity,
                                   card_number, artist,
                                   community_rating, number_of_voters, image_url)
                    bisect.insort(name_list, card_name)
                end = time.time()
                time_taken = end - start
                total_seconds = total_seconds + time_taken
                print("Added " + card_name + " without issue, total time for scrape and entry: " + str(time_taken)
                      + " seconds. Total time elapsed: " + str(
                    total_seconds) + " seconds . This card is Number: " + str(count))

        pages = driver.find_element_by_class_name("pagingcontrols")
        pages = pages.find_elements_by_tag_name("a")
        print("\n")
        print("Current Page: " + str(f))
        for j in pages:
            if j.text.isnumeric():
                if int(j.text) > f:
                    privacy_button = driver.find_element_by_class_name("close-me")
                    privacy_button.click()
                    print("Target Page: " + str(j.text))
                    j.click()
                    win_list = driver.window_handles
                    driver.switch_to.window(win_list[-1])
                    break

        print("Current average time taken: " + str(total_seconds / count))
        print("\n")
    driver.close()

    print("Total scrape done hooray!! That took way too long :p")


def load_into_mongodb():
    data = ""
    with open('mongoDB.txt', 'r') as file:
        data = file.read().replace('\n', '')

    client = MongoClient(data, tlsCAFile=certifi.where())
    mydatabase = client["MTGCards"]
    if "Card Information" in mydatabase.list_collection_names():
        connection = mydatabase["Card Information"]
        connection.drop()
    col = mydatabase["Card Information"]
    return client


def add_to_mongodb(mongo_client, card_name, mana, cmc, super_type, main_type, sub_type, card_text, flavor_text, set,
                   other_sets, rarity,
                   card_number,
                   artist, community_rating, number_of_voters, image_url):
    database = mongo_client["MTGCards"]
    card_info = database['Card Information']
    doc = {"Card Name": card_name,
           "Mana Cost": mana,
           "Converted Mana Cost": cmc,
           "Super Type": super_type,
           "Main Type": main_type,
           "Sub Type": sub_type,
           "Card Text": card_text,
           "Flavor Text": flavor_text,
           "Set": set,
           "Other Sets": other_sets,
           "Rarity": rarity,
           "Card Number": card_number,
           "Artist": artist,
           "Community Rating": community_rating,
           "Number of Voters": number_of_voters,
           "Image URL": image_url,
           }
    check_type(card_name, "name")
    check_type(mana, "mana")
    check_type(cmc, "cmc")
    check_type(super_type, "super type")
    check_type(main_type, "main type")
    check_type(sub_type, "sub type")
    check_type(card_text, "text")
    check_type(flavor_text, "flavor")
    check_type(set, "set")
    check_type(other_sets, "other sets")
    check_type(rarity, "rarity")
    check_type(card_number, "card num")
    check_type(artist, "artist")
    check_type(community_rating, "rating")
    check_type(number_of_voters, "voters")
    check_type(image_url, "url")
    card_info.insert_one(doc)


def check_type(thing, id):
    if type(thing) != int and type(thing) and type(thing) != float and type(thing) != str:
        print(id + " is not a string int or float")


def mongoDbToCSV(mongo_client):
    database = mongo_client["MTGCards"]
    card_info = database['Card Information']


def main():
    scrape()


def existsElement(id, driver):
    try:
        driver.find_element_by_id(id)
        return True
    except:
        return False


def existsTag(tag, element):
    try:
        element.find_elements_by_tag_name(tag)
        return True
    except:
        return False


def isElement(element, type):
    if element.tag_name == type:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
