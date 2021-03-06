from selenium.webdriver import Keys

from BaseApp import BasePage
from selenium.webdriver.common.by import By


class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_SUGGEST = (By.CSS_SELECTOR, ".mini-suggest__item")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
    LOCATOR_YANDEX_LINKS = (By.CSS_SELECTOR, ".organic__url")
    LOCATOR_YANDEX_LINKS_IMAGE = (By.XPATH, "/html/body/div[1]/div[2]/div[3]/div/div[2]/nav/div/ul/li[3]/a")
    LOCATOR_YANDEX_LINKS_IMAGE_POPULAR_REQUEST_LIST = (By.CSS_SELECTOR, ".PopularRequestList-Preview")


class SearchHelper(BasePage):
    # def open_link_popular(self):
    #     rzf = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_LINKS_IMAGE_POPULAR_REQUEST_LIST, time=2)
    #     return rzf
    #
    # def search_link_images(self):
    #     return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_LINKS_IMAGE)
    #
    # def click_link_images(self):
    #     return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_LINKS_IMAGE).click()

    def keys_enter(self):
        search_suggest = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_suggest.send_keys(Keys.ENTER)
        assert search_suggest != []

    def check_search_suggest(self):
        assert self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SUGGEST) != []

    def check_search_field(self):
        assert self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD) != []

    def enter_word(self, word):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        assert search_field != []

    def click_on_the_search_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=2).click()



    def check_link(self):
        all_list = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_LINKS, time=2)
        new_list = [item.get_attribute("href") for item in all_list[:5]]
        for elem in new_list:
            if elem.rfind('tensor.ru') == -1:
                assert False
