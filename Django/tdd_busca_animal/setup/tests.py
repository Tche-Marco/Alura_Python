from django.test import LiveServerTestCase
from selenium import webdriver


class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(
            'C:/Users/Marco Antônio/Desktop/Alura_Python/Django/tdd_busca_animal/chromedriver.exe'
        )

    def tearDown(self):
        self.browser.quit()

    def test_buscando_um_novo_animal(self):
        home_page = self.browser.get(self.live_server_url + '/')
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca Animal', brand_element.text)
