#!/usr/bin/python3
"""Gets the X-Request-Id header from a URL."""

import requests
import sys

def get_request_id(url):
  """Gets the X-Request-Id header from a URL.

  Args:
    url: The URL to get the request id from.

  Returns:
    The X-Request-Id header, or None if the header is not found.
  """

  try:
    res = requests.get(url)
    x_request_id = res.headers.get('X-Request-Id')
  except requests.exceptions.RequestException as e:
    print('Error: {}'.format(e))
    sys.exit(1)

  return x_request_id

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print('Usage: python script.py <url>')
    sys.exit(1)

  url = sys.argv[1]
  x_request_id = get_request_id(url)
  if x_request_id:
    print(x_request_id)
  else:
      print('None')