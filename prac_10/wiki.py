"""
wiki py
ask user for search query which searches wikipedia using their api and returns a summary
"""

import wikipedia

# ask user search
user_search = input("Search: ")

# check if blank, means end
while user_search != "":
    result = ""
    # use wikipedia api to search for wikipedia summary
    # error check if DisambiguationError
    try:
        result = wikipedia.page(user_search)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)

    # if found, no error, print title, summary and url
    print(f"Title: {result.title}")

    print(f"Summary: {result.summary}")

    print(f"URL: {result.url}")

    # ask user search after previous was found
    user_search = input("Search: ")

print(f"End")
