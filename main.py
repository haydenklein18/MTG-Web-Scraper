from selenium import webdriver
import os


def scrape():
    driver = webdriver.Chrome("C:/Users/kleinh/Downloads/chromedriver_win32/chromedriver.exe")
    URL = "https://gatherer.wizards.com/Pages/Search/Default.aspx?action=advanced&name=|[a]|[b]|[c]|[d]|[e]|[f]|[g]|[h]|[i]|[j]|[k]|[l]|[m]|[n]|[o]|[p]|[q]|[r]|[s]|[t]|[u]|[v]|[w]|[x]|[y]|[z]"
    driver.get(URL)
    win_list = driver.window_handles
    driver.switch_to.window(win_list[-1])
    for f in range(1, 215):
        for x in range(100):
            if x < 10:
                x = "0" + str(x)
            link = driver.find_element_by_id(
                "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl00_listRepeater_ctl" + str(x) + "_cardTitle")
            link.click()
            win_list = driver.window_handles
            driver.switch_to.window(win_list[-1])
            try:
                name_ele = driver.find_element_by_id(
                    "ctl00_ctl00_ctl00_MainContent_SubContent_SubContentHeader_subtitleDisplay")
                name = name_ele.text
                name = name.replace("\"", "")
                print("Card Name: " + name)
            except:
                print("", end='')

            try:
                big_mana = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_manaRow")
                mana_ele = big_mana.find_element_by_class_name("value")
                mana_list = mana_ele.find_elements_by_tag_name("img")
                print("Mana: ", end="")
                for z in mana_list:
                    print(z.get_attribute("alt") + " ", end='')

            except:
                print("", end='')

            try:
                cmc = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_cmcRow")
                cmc_ele = cmc.find_element_by_class_name("value")
                print("\nCMC:" + cmc_ele.text)
            except:
                print("", end='')

            try:
                card_text = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_textRow")
                card_text_ele = card_text.find_element_by_class_name("value")
                card_text_box0 = card_text_ele.find_elements_by_class_name("cardtextbox")
                card_text_box = ""
                for y in card_text_box0:
                    children = y.find_elements_by_xpath(".//*")
                    for x in children:
                        if isElement(x,"img"):
                            card_text_box += x.get_attribute("alt")+" "
                        elif isElement(x,"i"):
                            print("",end="")
                        else:
                            card_text_box += x.text+" "
                    card_text_box += y.text+" "
                print("Card Text: " + card_text_box)
            except:
                print("", end='')

            try:
                flavor = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_FlavorText")
                flavor_box = flavor.find_element_by_class_name("flavortextbox")
                print("Flavor Text: " + flavor_box.text)
            except:
                print("", end="")

            try:
                set = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_currentSetSymbol")
                print("Set: " + set.text)
            except:
                print("", end='')

            try:
                other_sets = driver.find_element_by_id(
                    "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_otherSetsValue")
                sets_ele = other_sets.find_elements_by_tag_name("img")
                print("Other Sets: ", end="")
                for x in sets_ele:
                    print(x.get_attribute("alt"), end="")
            except:
                print("", end='')

            try:
                rarity = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_rarityRow")
                rarity_ele = rarity.find_element_by_class_name("value")
                rarity_span = rarity_ele.find_elements_by_tag_name("span")
                print("Rarity: " + rarity_span[0].text)
            except:
                print("", end='')

            try:
                card_num = driver.find_element_by_id(
                    "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_CardNumberValue")
                print("Card Number: " + card_num.text)
            except:
                print("", end='')

            try:
                artist = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ArtistCredit")
                artist_ele = artist.find_element_by_tag_name("a")
                print("Artist: " + artist_ele.text)
            except:
                print("", end='')

            try:
                rating = driver.find_element_by_id(
                    "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_currentRating_textRating")
                print("Community Rating: " + rating.text + "/5")
            except:
                print("", end='')

            dual_card_bool = existsElement("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl03_cardImage",
                                           driver)
            if dual_card_bool:
                png = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl02_cardImage")
            else:
                png = driver.find_element_by_id("ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_cardImage")
            alt = png.get_attribute("alt")
            alt = alt.replace("\"", "")

            if not dual_card_bool:
                with open(alt + ".png", 'wb') as file:
                    file.write(driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_cardImage").screenshot_as_png)
            else:
                with open(alt + ".png", 'wb') as file:
                    file.write(driver.find_element_by_id(
                        "ctl00_ctl00_ctl00_MainContent_SubContent_SubContent_ctl02_cardImage").screenshot_as_png)

            driver.execute_script("window.history.go(-1)")
            print("\n")

            os.remove(alt + ".png")
        pages = driver.find_element_by_class_name("pagingcontrols")
        pages = pages.find_elements_by_tag_name("a")
        print("Current Page: " + str(f))
        for j in pages:
            if j.text.isnumeric():
                if int(j.text) > f:
                    print("Target Page: " + str(j.text))
                    print("\n")
                    j.click()
                    win_list = driver.window_handles
                    driver.switch_to.window(win_list[-1])
                    break
    driver.close()


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
