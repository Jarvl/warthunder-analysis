# from abc import ABC, abstractmethod
from functools import wraps
from bs4 import BeautifulSoup


class GroundVehicleExtraction:
  MAIN_INFO_DIV = '#mw-content-text > div.mw-parser-output > div.specs_card_main > div.specs_card_main_info'
  GENERAL_INFO_DIV = f'{MAIN_INFO_DIV} > div.general_info'
  GENERAL_INFO_2_DIV = f'{MAIN_INFO_DIV} > div.general_info_2'
  BATTLE_RATING_TR = f'{GENERAL_INFO_2_DIV} > div.general_info_br > table > tbody > tr:nth-child(2)'
  DATA_POINTS = (
    'name',
    'country',
    'rank',
    'classification',
    'battle_rating_AB',
    'battle_rating_RB',
    'battle_rating_SB',
    'purchase',
    'armour_mm_hull',
    'armour_mm_turret',
    'crew_num',
    'visibility'
  )

  @classmethod
  def extract_from_html(cls, html: str):
    soup = BeautifulSoup(html, 'html5lib')
    return (
      cls.__select_first_text(soup, f'{cls.MAIN_INFO_DIV} > div.general_info_name'),
      cls.__select_first_text(soup, f'{cls.GENERAL_INFO_DIV} > div.general_info_nation > a:nth-child(2)'),
      cls.__select_first_text(soup, f'{cls.GENERAL_INFO_DIV} > div.general_info_rank > a:first-child'),
      cls.__select_first_text(soup, f'{cls.GENERAL_INFO_2_DIV} > div.general_info_class > div:last-child > a'),
      cls.__select_first_text(soup, f'{cls.BATTLE_RATING_TR} > td:nth-child(1)'),
      cls.__select_first_text(soup, f'{cls.BATTLE_RATING_TR} > td:nth-child(2)'),
      cls.__select_first_text(soup, f'{cls.BATTLE_RATING_TR} > td:nth-child(3)'),
      cls.__select_first_text(soup, f'{cls.MAIN_INFO_DIV} > div.general_info_price > div > span.value'),
      cls.__select_spec(soup, 'Survivability_and_armour', 'Hull'),
      cls.__select_spec(soup, 'Survivability_and_armour', 'Turret'),
      cls.__select_spec(soup, 'Survivability_and_armour', 'Crew'),
      cls.__select_spec(soup, 'Survivability_and_armour', 'Visibility'),
    )
  
  @classmethod
  def __select_spec(cls, soup: BeautifulSoup, preceding_heading_id: str, name: str):
    return soup.find(id=preceding_heading_id).find_next('span', {'class': 'name'}, text=name).find_next_sibling('span').get_text()
  
  @classmethod
  def __select_first_text(cls, soup: BeautifulSoup, selector: str):
    return soup.css.select_one(selector).get_text()
