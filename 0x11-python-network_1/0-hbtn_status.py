#!/usr/bin/python3
"""Python script that fetches https"""


import urllib.request
if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        data = response.read()
        decoded_data = data.decode('utf-8')

    print('Body response:')
    print('\t- type: {}'.format(type(data)))
    print('\t- content: {}'.format(data))
    print('\t- utf8 content: {}'.format(decoded_data))
