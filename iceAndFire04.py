#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        if got_dj["name"]:
            print(got_dj["name"])
        else:
            print(", ".join(got_dj['aliases']))
        


        # get houses- pull out "allegiances" from response - it's a list and use to make api call for houses
        if len(got_dj["allegiances"]) == 1:
            houseUrl = got_dj["allegiances"][0]

            gethouse = requests.get(houseUrl)
            got_house = gethouse.json()
            print("Allegiance: ", got_house["name"])
        elif len(got_dj["allegiances"]) > 1:
            houses = []
            for allegiance in got_dj["allegiances"]:
                gethouse = requests.get(allegiance)
                got_house = gethouse.json()
                houses.append(got_house["name"])
            print("Allegiances: ", ", ".join(houses))
        else:
            print("No Allegiances")
        
        #pull out books list from response and use to make api call for the book(s) character appears in
        
        if len(got_dj['books']) == 1:
            bookUrl = got_dj["books"][0]
            getbook = requests.get(bookUrl)
            got_book = getbook.json()
            print("Appearing in book: ", got_book["name"])
        elif len(got_dj['books']) > 1:
            books =[]
            for book in got_dj["books"]:
                getbook = requests.get(book)
                got_book = getbook.json()
                books.append(got_book["name"])
            print("Appearing in books: ",", ".join(books))

if __name__ == "__main__":
        main()

