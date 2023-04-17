# TCGPlayer-Order-History-Analyzer
'Web' Scraper that will extract the date of an order, the individual items within an order, purchase price per item, and some details about the item.

This script functions by opening an already downloaded html file of the TCGPlayer Order History web page. Unfortunately, the TCGPlayer api is not open,
and selenium is stopped immediately upon login because of the bot login protection. (Maybe I could've done it pre logged in but that didnt sound cool).
The script ensures to go through each .html file in the set directory, and parses through them and extracts order date, card name, card price, and card
set.

Then, I loop through each card that was added to my dictionary and find its current price using the Scryfall API. Finishing off with a .csv export.

Unforunately, since there are often multiple variants to any one card, and each variant having oen of many treatments, it may not be the most accurate but
I had to work with what I had. This at the very least provides me with a close approximation.
