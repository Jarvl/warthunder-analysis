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
    self.extractors = {
      'name': self.__select_first_text(f'{MAIN_INFO_DIV} > div.general_info_name'),
      'country': self.__select_first_text(f'{GENERAL_INFO_DIV} > div.general_info_nation > a:nth-child(2)'),
      'rank': self.__select_first_text(f'{GENERAL_INFO_DIV} > div.general_info_rank > a:first-child'),
      'classification': self.__select_first_text(f'{GENERAL_INFO_2_DIV} > div.general_info_class > div:last-child > a'),
      'battle_rating_AB': self.__select_first_text(f'{BATTLE_RATING_TR} > td:nth-child(1)'),
      'battle_rating_RB': self.__select_first_text(f'{BATTLE_RATING_TR} > td:nth-child(2)'),
      'battle_rating_SB': self.__select_first_text(f'{BATTLE_RATING_TR} > td:nth-child(3)'),
      'purchase': self.__select_first_text(f'{MAIN_INFO_DIV} > div.general_info_price > div > span.value'),
      'armour_hull': self.__select_armour('Hull'),
      'armour_turret': self.__select_armour('Turret'),
    }
  
  def __select_armour(self, name):
    return lambda: self.soup.find('span', {'class': 'name'}, text=name).find_next_sibling('span').get_text()
  
  def __select_first_text(self, selector):
    return lambda: self.soup.css.select_one(selector).get_text()

  def extract_all(self):
    return { data_point: func() for data_point, func in self.extractors.items() }
