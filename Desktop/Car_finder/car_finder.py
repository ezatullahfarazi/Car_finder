from car_generator import *
import requests, webbrowser
from urllib.parse import quote

api_key = "AIzaSyC45e7FXeiqzeWhXokwhC_fdr8pr--WUSQ"
search_engine_id = "a40dfe24c629549bd"

query = get_car()
encoded_query = quote(query)

url = f"https://www.googleapis.com/customsearch/v1?q={encoded_query}&key={api_key}&cx={search_engine_id}"

response = requests.get(url)

if response.status_code == 200:
    search_result = response.json() # Creates a json file of all the searched results
    searched_items = search_result.get("items", []) # Get item or return an empty list instead of crashing
    # The above line are car webpages

    # Now, we have a file that contains car links. Let's show the first item (car webpage) to the user, by opening user's browser
    if searched_items:
        first_result_link = searched_items[0].get("link")
        webbrowser.open(first_result_link) # Printing the first item on user's browser
    else:
        print("No results found.")
else:
    print(f"Error: {response.status_code}, {response.text}")