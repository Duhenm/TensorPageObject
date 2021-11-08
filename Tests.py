from YandexPages import SearchHelper

def test_tensor_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.check_search_field()
    yandex_main_page.enter_word("Тензор")
    yandex_main_page.check_search_suggest()
    yandex_main_page.keys_enter()
    elements = yandex_main_page.check_link()
    assert "tensor.ru" in elements

def test_image_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.search_link_images()
    # yandex_main_page.click_link_images()
    # yandex_main_page.open_link_popular()
    print('   ')

