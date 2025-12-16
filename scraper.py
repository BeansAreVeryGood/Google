import asyncio
from playwright.async_api import async_playwright
import requests
from bs4 import BeautifulSoup
import json

def get_unit_urls(faction):
    url = f"https://wahapedia.ru/wh40k10ed/factions/{faction}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)
    unit_urls = []
    for link in links:
        href = link['href']
        if href.startswith(f"/wh40k10ed/factions/{faction}/") and href != f"/wh40k10ed/factions/{faction}/":
            full_url = "https://wahapedia.ru" + href
            unit_urls.append(full_url)
    return unit_urls[:5]  # First 5

async def get_unit_data(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        # Wait for the page to load
        await page.wait_for_load_state('networkidle')
        # Evaluate the datasheet variable
        data = await page.evaluate('datasheet')
        await browser.close()
        return data

async def main():
    selected_units = []

    # Space Marines
    sm_urls = get_unit_urls('space-marines')
    for url in sm_urls:
        unit = await get_unit_data(url)
        selected_units.append({
            "name": unit.get("name"),
            "points": unit.get("cost"),
            "battlefield_role": unit.get("role"),
            "keywords": unit.get("keywords", []),
            "statline": unit.get("stats"),
            "weapons": unit.get("weapons", []),
            "abilities": unit.get("abilities", {}),
            "lore": unit.get("lore", "")
        })

    # Orks
    ork_urls = get_unit_urls('orks')
    for url in ork_urls:
        unit = await get_unit_data(url)
        selected_units.append({
            "name": unit.get("name"),
            "points": unit.get("cost"),
            "battlefield_role": unit.get("role"),
            "keywords": unit.get("keywords", []),
            "statline": unit.get("stats"),
            "weapons": unit.get("weapons", []),
            "abilities": unit.get("abilities", {}),
            "lore": unit.get("lore", "")
        })

    print(json.dumps(selected_units, indent=4))

asyncio.run(main())