#!/usr/bin/env python3

import requests

def main():
    starwarsplanets = requests.get("https://swapi.dev/api/planets/1/")
    print(starwarsplanets)





if __name__ == "__main__":
    main()
