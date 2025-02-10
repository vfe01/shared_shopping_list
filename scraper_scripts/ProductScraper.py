
import requests
from bs4 import BeautifulSoup
from WrongDomainException import WrongDomainException
from AmbiguousIdentifierException import AmbiguousIdentifierException
from NoTagFoundException import NoTagFoundException
from abc import ABC, abstractmethod

class ProductScraper(ABC):
    def __init__(self, url, expected_domain):
        domain = url.split("/")[2]
        if domain != expected_domain:
            raise WrongDomainException(f"Expected domain {expected_domain} but got {domain}.")
        self._url = url
        response = requests.get(url)
        #TODO: error handling for request
        self._soup:BeautifulSoup = BeautifulSoup(response.content, 'html.parser')

    @abstractmethod
    def get_name(self):
        pass
    
    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_image(self):
        pass
    
    @abstractmethod
    def get_url(self):
        pass

    def find_unique(self, attribute_value_dict, bs=None):
        if bs==None:
            bs = self._soup
        div = bs.find_all(attrs=attribute_value_dict)
        if len(div) == 0:
            raise NoTagFoundException()
        if len(div) != 1:
            raise AmbiguousIdentifierException()
        div = div[0]
        return div

