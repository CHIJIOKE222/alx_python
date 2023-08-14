#!/usr/bin/python3
"""this program uses the GitHub API to display my id"""
import requests
import sys
def get_github_id(username, password):
    """Gets the GitHub id for the specified username and password."""
    url = 'https://api.github.com/users/{}'.format(username)
    auth = requests.auth.HTTPBasicAuth(username, password)
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        return response.json()['id']
    else:
        if response.status_code == 401:
            print('None')
        else:
            print('Error getting GitHub id: {}'.format(response.status_code))
            sys.exit(1)

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    id = get_github_id(username, password)
    print('{}'.format(id))