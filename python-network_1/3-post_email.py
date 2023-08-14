#!/usr/bin/python3
"""Sends a POST request to the specified URL with the specified email address as a parameter."""

import requests
import sys

def post_email(url, email):
  """Sends a POST request to the specified URL with the specified email address as a parameter."""
  data = {"email": email}
  res = requests.post(url, data=data)
  return res

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Usage: python script.py <url> <email>")
    sys.exit(1)

  url = sys.argv[1]
  email = sys.argv[2]

  res = post_email(url, email)
  print(res.text)