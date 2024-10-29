# Part 1: Data Collection Through Web Scraping
## Make Necessary Imports
import re
import requests
import time
import json
from bs4 import BeautifulSoup

## Function to Extract Specific HTML Element
def get_text(selector):
    element = pokemon_soup.select_one(selector)
    return element.text.strip() if element else 'N/A'

## Make Request To Pokemon Page
url = 'https://pokemondb.net/pokedex/all'
print("Starting Data Scraping for...", url)

response = requests.get(url)        # request to fetch the webpage
response.raise_for_status()         # raise error for 500 response

# parse the content with BeautifulSoup
pokemon_all = BeautifulSoup(response.content, 'html.parser')

## Data Extraction
pokemon_links = []
# find all Pokémon links
for i in pokemon_all.select('table#pokedex tbody tr a[href^="/pokedex/"]'):
    pokemon_links.append(i['href'])

# print first 10 links to verify
print("\nPrinting first 10 pokemon_links...")
index = 0
for link in pokemon_links[:10]:
    index += 1
    print(index, ":", link)

## Individual Pokemon Scraping
pokemon_data = {}
# setting the limit to scrape max 50 Pokemons
max_pokemons = 10
print()
for link in pokemon_links[:max_pokemons]:
    # wait for 5 seconds between requests
    time.sleep(5)
    pokemon_link = 'https://pokemondb.net' + link
    response = requests.get(pokemon_link)
    response.raise_for_status()
    pokemon_soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the Data
    # Pokedex Data
    name = pokemon_soup.find('h1').text
    national_no = get_text('table.vitals-table tr:-soup-contains("National №") td')

    # Scraping types
    type_elements = pokemon_soup.select('table.vitals-table tr:-soup-contains("Type") td a')
    types = [type_element.get_text(strip=True).lower() for type_element in type_elements]
    species = get_text('table.vitals-table tr:-soup-contains("Species") td')
    height = get_text('table.vitals-table tr:-soup-contains("Height") td').replace('\xa0', ' ').strip()
    weight = get_text('table.vitals-table tr:-soup-contains("Weight") td').replace('\xa0', ' ').strip()

    # Modify the extraction for abilities
    abilities = get_text('table.vitals-table tr:-soup-contains("Abilities") td')
    # Remove numbers and hidden text
    abilities_cleaned = re.sub(r'\d+\.\s*|\s*\(hidden ability\)', '', abilities)
    # Add comma before capital letter
    abilities_cleaned = re.sub(r'(?<=\w)(?=[A-Z])', ', ', abilities_cleaned).strip()

# Training
    ev_yield = get_text('table.vitals-table tr:-soup-contains("EV yield") td')
    catch_rate = get_text('table.vitals-table tr:-soup-contains("Catch rate") td')
    base_friendship = get_text('table.vitals-table tr:-soup-contains("Base") td')
    base_exp = get_text('table.vitals-table tr:-soup-contains("Base Exp.") td')
    growth_rate = get_text('table.vitals-table tr:-soup-contains("Growth Rate") td')

    # Breeding
    egg_groups = get_text('table.vitals-table tr:-soup-contains("Egg Groups") td')
    gender = get_text('table.vitals-table tr:-soup-contains("Gender") td')
    egg_cycles = get_text('table.vitals-table tr:-soup-contains("Egg cycles") td').strip()

    # Base Stats
    hp = get_text('table.vitals-table tr:-soup-contains("HP") td.cell-num:nth-of-type(1)')
    attack = get_text('table.vitals-table tr:-soup-contains("Attack") td.cell-num:nth-of-type(1)')
    defense = get_text('table.vitals-table tr:-soup-contains("Defense") td.cell-num:nth-of-type(1)')
    sp_atk = get_text('table.vitals-table tr:-soup-contains("Sp. Atk") td.cell-num:nth-of-type(1)')
    sp_def = get_text('table.vitals-table tr:-soup-contains("Sp. Def") td.cell-num:nth-of-type(1)')
    speed = get_text('table.vitals-table tr:-soup-contains("Speed") td.cell-num:nth-of-type(1)')
    total = get_text('table.vitals-table tfoot tr th:-soup-contains("Total") + td.cell-num.cell-total')

    # Evo Chart
    evo_elements = pokemon_soup.select('div.infocard-list-evo div.infocard a.ent-name')
    evo_path = [evo_element.get_text(strip=True) for evo_element in evo_elements]

    ######## NOTE ########
    ### Im removing "moves" from scraped data purposely, as this field is quite excessive. It makes the rest of my assignment messy. ###
    ### To see that scraping for "moves" works, please uncomment the lines "move_elements" and "moves"
    ### "moves" also needs to be uncommented in pokemon_data
    ######## NOTE ########
    # Moves
    # move_elements = pokemon_soup.select('table.data-table tbody tr td.cell-name a.ent-name')
    # moves = [move_element.get_text(strip=True) for move_element in move_elements]

    # Pokemon Image
    img_tag = pokemon_soup.select_one('div.grid-col.span-md-6.span-lg-4.text-center img')
    if img_tag:
        pokemon_img_url = img_tag['src']
    else:
        pokemon_img_url = None

    pokemon_data[name.lower()] = {
        "name": name.lower(),
        "national_no": national_no,
        "types": types,
        "species": species,
        "height": height,
        "weight": weight,
        "abilities": abilities_cleaned,
        "ev_yield": ev_yield,
        "catch_rate": catch_rate,
        "base_friendship": base_friendship,
        "base_exp": base_exp,
        "growth_rate": growth_rate,
        "egg_groups": egg_groups,
        "gender": gender,
        "egg_cycles": egg_cycles.replace("\t", ""),
        "hp": hp,
        "attack": attack,
        "defense": defense,
        "sp_atk": sp_atk,
        "sp_def": sp_def,
        "speed": speed,
        "total": total,
        "evo_path": evo_path,
        #"moves": moves,
        "pokemon_img_url": pokemon_img_url
    }
    print(f"Scraped data for: {name}")
print("\nData scraping completed successfully\n")

# print first 10 Pokémon data to verify
print("Verifying first 10 Pokemons in JSON file...\n")
index = 0
for pokemon in list(pokemon_data.keys())[:10]:
    index += 1
    print(pokemon_data[pokemon]['name'], ":", pokemon_data[pokemon])

## Save Scraped Data in JSON Format
file_name = "pokemon_data.json"
with open(file_name, 'w') as json_file:
    json.dump(pokemon_data, json_file, indent=4)

print('\n', file_name, 'file was successfully saved')

