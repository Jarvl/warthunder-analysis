import os
import hashlib
import aiofiles
import aiohttp
from bs4 import BeautifulSoup

WT_WIKI_URL = 'https://wiki.warthunder.com/'
VEHICLE_LINKS_SELECTOR = '#mw-content-text > div.mw-parser-output > table > tbody > tr:not(:first-child) > td:nth-child(2) > a'


def data_dir():
  return os.path.join(os.path.abspath(''), '..', 'data')


async def read_file(filename: str):
  async with aiofiles.open(filename, mode='r') as f:
    return await f.read()


async def write_file(filename: str, contents: str):
  os.makedirs(os.path.dirname(filename), exist_ok=True)
  async with aiofiles.open(filename, mode='w') as f:
    return await f.write(contents)


async def fetch_text_from_url(url: str, session: aiohttp.ClientSession | None = None):
  async def call():
    async with session.get(url, raise_for_status=True) as resp:
      return await resp.text()

  if session is None:
    async with aiohttp.ClientSession() as session:
      return await call()
  else:
    return await call()


async def parse_html_from_url(url: str, session: aiohttp.ClientSession | None = None):
  contents = await fetch_text_from_url(url, session)
  return BeautifulSoup(contents, 'html5lib')


async def generate_premium_ground_vehicle_urls():
  soup = await parse_html_from_url(f"{WT_WIKI_URL}Category:Premium_ground_vehicles")
  a_tags = soup.css.select(VEHICLE_LINKS_SELECTOR)
  return [f"{WT_WIKI_URL}{a.get('href').lstrip('/')}" for a in a_tags]


async def cache_vehicle_html(url: str, html_path: str, session: aiohttp.ClientSession | None = None, overwrite: bool = False):
  contents = await fetch_text_from_url(url, session)
  # Some vehicles have a `/` in them so they are normalized to hashes
  hashed_url = hashlib.md5(url.encode('utf-8')).hexdigest()
  html_filename = os.path.join(html_path, f'{hashed_url}.html')

  if overwrite or not os.path.isfile(html_filename):
    await write_file(html_filename, contents)
