from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

import enum




class GroundVehicleExtraction:
  MAIN_INFO_DIV = '#mw-content-text > div.mw-parser-output > div.specs_card_main > div.specs_card_main_info'

  def __init__(self, html: str) -> None:
    self.soup = BeautifulSoup(html, 'html5lib')

  def select(self, *args):
    return self.soup.css.select(*args)

  @property
  def name(self):
    selector = f'{self.MAIN_INFO_DIV} > div.general_info_name'
    return self.select(selector)[0].get_text()

  @property
  def country(self):
    selector = f'{self.MAIN_INFO_DIV} > div.general_info > div.general_info_nation > a:nth-child(2)'
    return self.select(selector)[0].get_text()

  # @property
  # def type(self):
  #   selector = f'{self.MAIN_INFO_DIV} > div.general_info > div.general_info_rank > a:first-child'
  #   return self.select(selector)[0].get_text()

  @property
  def rank(self):
    selector = f'{self.MAIN_INFO_DIV} > div.general_info > div.general_info_rank > a:first-child'
    return self.select(selector)[0].get_text()

class Extractor(ABC):
  def __init__(self) -> None:
    super().__init__()

  @abstractmethod
  def extract(self) -> any:
    pass


class BasicInfoComponent(Extractor):
  @property
  def name(self) -> str:
    pass

  @property
  def country(self) -> str:
    pass

  @property
  def rank(self) -> str:
    pass

  @property
  def battle_rating(self) -> str:
    pass

  @property
  def is_premium(self) -> str:
    pass

  # Research cost relies on this (silver lions)
  @property
  def purchase_type(self) -> str:
    pass

  @abstractmethod
  def extract(self) -> dict:
    pass


class Vehicle:
  def __init__(self) -> None:
    self.basic_info = BasicInfoComponent()


class GroundVehicle(Vehicle, Extractor):
  @property
  def classification(self) -> str:
    pass

  @abstractmethod
  def extract(self) -> any:
    pass


class AirVehicle(Vehicle, Extractor):
  @property
  def classification(self) -> str:
    pass

  @property
  def max_altitude(self) -> str:
    pass

  @abstractmethod
  def extract(self) -> any:
    pass


class Vehicle(Extractor):
  def __init__(self, vehicle_type_component_cls: VehicleTypeComponent) -> None:
    self.children = [BasicsComponent(), vehicle_type_component_cls()]

  def extract(self) -> list: # TODO: should be dict
    [child.extract() for child in self.children]


# class Vehicle(ABC):
#   @abstractmethod
#   def name(self) -> str:
#     pass

#   @abstractmethod
#   def country(self) -> str:
#     pass

#   @abstractmethod
#   def rank(self) -> str:
#     pass

#   @abstractmethod
#   def rank(self) -> str:
#     pass


class GroundVehicle(Vehicle):
  def extract(self) -> str:
    pass


class AirVehicle(Vehicle):
  def extract(self) -> str:
    pass


class Extractor:
  def create_extractor(self, vehicle_cls: Vehicle) -> None:
    return vehicle_cls()