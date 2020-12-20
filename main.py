from selenium import webdriver


def scrape():
    driver = webdriver.Chrome("C:/Users/kleinh/Downloads/chromedriver_win32/chromedriver.exe")
    URL = "https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&name=|[a]|[b]|[c]|[d]|[e]|[f]|[g]|[h]|[i]|[j]|[k]|[l]|[m]|[n]|[o]|[p]|[q]|[r]|[s]|[t]|[u]|[v]|[w]|[x]|[y]|[z]"
    driver.get(URL)
    link = driver.find_element_by_id(
        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl00_listRepeater_ctl00_cardTitle")
    link.click()
    name_ele = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContentHeader_subtitleDisplay")
    name = name_ele.text
    name = name.replace("\"","")
    print(name)
    big_mana = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_manaRow")
    mana_ele = big_mana.find_element_by_class_name("value")
    mana_list = mana_ele.find_elements_by_tag_name("img")
    for x in mana_list:
        print(x.get_attribute("alt"))

    cmc = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_cmcRow")
    cmc_ele = cmc.find_element_by_class_name("value")
    print(cmc_ele.text)

    card_text = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_textRow")
    card_text_ele = card_text.find_element_by_class_name("value")
    card_text_box = card_text_ele.find_element_by_class_name("cardtextbox")
    print(card_text_box.text)

    set = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_currentSetSymbol")
    print(set.text)

    rarity = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_rarityRow")
    rarity_ele = rarity.find_element_by_class_name("value")
    rarity_span = rarity_ele.find_elements_by_tag_name("span")
    print(rarity_span[0].text)

    card_num = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_CardNumberValue")
    print(card_num.text)

    artist = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ArtistCredit")
    artist_ele = artist.find_element_by_tag_name("a")
    print(artist_ele.text)

    rating = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_currentRating_textRating")
    print(rating.text+"/5")

    with open(name+".png", 'wb') as file:
        file.write(driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_cardImage").screenshot_as_png)

    driver.execute_script("window.history.go(-1)")


    driver.close()


def main():
    scrape()


if __name__ == '__main__':
    main()
