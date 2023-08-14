#!/usr/bin/python3
"""Sends a POST request to the specified URL and prints the body of the response.

If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
"""
import requests
import sys
def search_user(letter):
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data={'q': letter})
    return response

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("No result")
        sys.exit(1)

    letter = sys.argv[1]

    response = search_user(letter)
    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No Result")
    except ValueError:
        print("Not a valid JSON")