import requests
"""
Update source from below URL.
"""


def get_oui_data():
    url = 'https://standards-oui.ieee.org/oui/oui.csv'
    r = requests.get(url, stream=True).content
    with open('oui.db', 'wb') as db:
        db.write(r)
    db.close()


