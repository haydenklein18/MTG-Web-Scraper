from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient
import time


def scrape():
    count = 0
    total_seconds = 0
    mongo_client = load_into_mongodb()
    options = Options()
    options.headless = True
    driver = webdriver.Chrome("C:/Users/kleinh/Downloads/chromedriver_win32/chromedriver.exe", options=options)
    URL = "https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&name=|[a]|[b]|[c]|[d]|[e]|[f]|[g]|[h]|[i]|[j]|[k]|[l]|[m]|[n]|[o]|[p]|[q]|[r]|[s]|[t]|[u]|[v]|[w]|[x]|[y]|[z] "
    driver.get(URL)
    win_list = driver.window_handles
    driver.switch_to.window(win_list[-1])
    for f in range(1, 215):
        for x in range(100):
            count = count + 1
            start = time.time()
            card_name = ""
            mana = ""
            cmc = -1
            card_text = ""
            flavor_text = ""
            set = ""
            other_sets = ""
            rarity = ""
            card_number = -1
            artist = ""
            community_rating = -1.0
            number_of_voters = -1
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
            print(dual_card_bool)
            print(modal_card_bool)
            if dual_card_bool:
                print("dual")
                # TODO Write Support for dual cards
            elif modal_card_bool:
                print("modal")
                # TODO Write Support for modal cards
            else:

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

                image_url = driver.find_element_by_id(
                    "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_cardImage").get_attribute("src")

                driver.execute_script("window.history.go(-2)")
                add_to_mongodb(mongo_client, card_name, mana, cmc, card_text, flavor_text, set, other_sets, rarity,
                               card_number, artist,
                               community_rating, number_of_voters, image_url)
                end = time.time()
                time_taken = end - start
                total_seconds = total_seconds + time_taken
                print("Added " + card_name + " without issue, total time time for scrape and entry: " + str(time_taken)
                      + " seconds. Total time elapsed: " + str(
                    total_seconds) + " seconds . This card is Number: " + str(count))

        pages = driver.find_element_by_class_name("pagingcontrols")
        pages = pages.find_elements_by_tag_name("a")
        print("\n")
        print("Current Page: " + str(f))
        for j in pages:
            if j.text.isnumeric():
                if int(j.text) > f:
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
    client = MongoClient(
        "mongodb+srv://rocketguitarist11:Rocketman25@cluster0.cne94.mongodb.net/MTGCards?retryWrites=true&w=majority")
    mydatabase = client["MTGCards"]
    if "Card Information" in mydatabase.list_collection_names():
        connection = mydatabase["Card Information"]
        connection.drop()
    col = mydatabase["Card Information"]
    return client


def add_to_mongodb(mongo_client, card_name, mana, cmc, card_text, flavor_text, set, other_sets, rarity, card_number,
                   artist, community_rating, number_of_voters, image_url):
    database = mongo_client["MTGCards"]
    card_info = database['Card Information']
    doc = {"Card Name": card_name,
           "Mana Cost": mana,
           "Converted Mana Cost": cmc,
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
