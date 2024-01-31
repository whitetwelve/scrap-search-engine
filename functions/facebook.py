# from bs4 import BeautifulSoup
# import requests

# def get_bing_search_link(predicted_class):
#     formatted_name = name.replace(' ', '%20')
#     url = "https://www.bing.com/search?q=" + formatted_name + "facebook"
#     return url

# def get_first_facebook_link(search_url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
#     }

#     content = requests.get(search_url, headers=headers).text
#     soup = BeautifulSoup(content, 'html.parser')

#     # Find the first search result link
#     first_link_container = soup.find('li', class_='b_algo')
#     first_link = first_link_container.find('a')['href'] if first_link_container else None

#     # Check if the link contains 'https://www.facebook.com'
#     if first_link and 'https://www.facebook.com' in first_link:
#         return first_link
#     else:
#         return None

# # Get the Bing search URL
# search_url = get_bing_search_link(predicted_class)

# # Get the first Instagram link from the search results
# first_facebook_link = get_first_facebook_link(search_url)

# if first_facebook_link:
#     print("First facebook link for", predicted_class, "is:", first_facebook_link)
# else:
#     print("No facebook link found for", predicted_class)
