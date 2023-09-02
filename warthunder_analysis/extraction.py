# from abc import ABC, abstractmethod
from functools import wraps
from bs4 import BeautifulSoup


MAIN_INFO_DIV = '#mw-content-text > div.mw-parser-output > div.specs_card_main > div.specs_card_main_info'
GENERAL_INFO_DIV = f'{MAIN_INFO_DIV} > div.general_info'
GENERAL_INFO_2_DIV = f'{MAIN_INFO_DIV} > div.general_info_2'
BATTLE_RATING_TR = f'{GENERAL_INFO_2_DIV} > div.general_info_br > table > tbody > tr:nth-child(2)'

class GroundVehicleExtraction:
  def __init__(self, html: str) -> None:
    self.soup = BeautifulSoup(html, 'html5lib')
    self.extractors = [
      ('name', f'{MAIN_INFO_DIV} > div.general_info_name', self.__select_first_text),
      ('country', f'{GENERAL_INFO_DIV} > div.general_info_nation > a:nth-child(2)', self.__select_first_text),
      ('rank', f'{GENERAL_INFO_DIV} > div.general_info_rank > a:first-child', self.__select_first_text),
      ('classification', f'{GENERAL_INFO_2_DIV} > div.general_info_class > div:last-child > a', self.__select_first_text),
      ('battle_rating_AB', f'{BATTLE_RATING_TR} > td:nth-child(1)', self.__select_first_text),
      ('battle_rating_RB', f'{BATTLE_RATING_TR} > td:nth-child(2)', self.__select_first_text),
      ('battle_rating_SB', f'{BATTLE_RATING_TR} > td:nth-child(3)', self.__select_first_text),
      ('purchase', f'{MAIN_INFO_DIV} > div.general_info_price > div > span.value', self.__select_first_text),
    ]

  def __select(self, *args):
    return self.soup.css.select(*args)
  
  def __select_first_text(self, *args):
    return self.__select(*args)[0].get_text()

  def extract_all(self):
    return { data_point: func(selector) for data_point, selector, func in self.extractors }
