from ProductScraper import ProductScraper
import unittest

class IkeaProductScraper(ProductScraper):

    def __init__(self, url):
        self._url = url
        super().__init__(url, "www.ikea.com")

    def get_name(self):
        product_title_div = self.find_unique(
            {
                "class":"pip-header-section__container-text"
            }
        )

        product_name = self.find_unique(
            {
                "class":"pip-header-section__title--big notranslate"
            },
            product_title_div
        ).text.replace(" ", "")

        product_description = self.find_unique(
            {
                "class":"pip-header-section__description-text"
            },
            product_title_div
        ).text
        return f"{product_name} ({product_description})"


    def get_price(self):
        price = self.find_unique(
            {
                "class": "pip-price__sr-text"
            }
        ).text
        return price


    def get_image(self):
        main_product_div = self.find_unique(
            {
                "data-type": "MAIN_PRODUCT_IMAGE"
            }
        )
        
        main_product_image = self.find_unique(
            {
                "class": "pip-image"
            },
            main_product_div
        )

        image_url = main_product_image["srcset"].split(",")[0].split(" ")[-2]
        
        return image_url

    def get_url(self):
        return self._url
    
    def get_all(self):
        return {
            "name": self.get_name(),
            "price": self.get_price(),
            "image": self.get_image(),
            "url": self.get_url()
        }

class TestIkeaProductScraper(unittest.TestCase):
    
    def setUp(self):
        self.ikea_scraper = IkeaProductScraper("https://www.ikea.com/se/sv/p/ombonad-skal-moerkgra-20502963/")
    
    def test_get_title(self):
        name = self.ikea_scraper.get_name()
        self.assertEqual(name, "OMBONAD (Skål, mörkgrå, )")

    def test_get_price(self):
        price = self.ikea_scraper.get_price()
        self.assertEqual(price, "Pris 99:-/2 styck")
        
    def test_get_image(self):
        image_link = self.ikea_scraper.get_image()
        self.assertEqual(image_link, "https://www.ikea.com/se/sv/images/products/ombonad-skal-moerkgra__1062740_pe850974_s5.jpg?f=xl")

    

if __name__ == '__main__':
    unittest.main()