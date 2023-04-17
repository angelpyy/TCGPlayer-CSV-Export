import requests


def get_price(card_name: str) -> int:
    # scryfall api search request
    price = -1
    response = requests.get(f'https://api.scryfall.com/cards/search?q={card_name}')

    # check response status code
    if response.status_code == 200:
        card_data = response.json()

        # card data
        if 'data' in card_data:
            # Get the first card from the list of cards returned by the API
            card = card_data['data'][0]

            # Check if the 'prices' key is present in the card data
            if 'prices' in card:
                # Get the USD price of the card, if available
                if 'usd' in card['prices']:
                    price = card['prices']['usd']
    else:
        # If the response was unsuccessful, print the status code
        print(f'Request failed with status code {card_name}: {response.status_code}')

    return price
