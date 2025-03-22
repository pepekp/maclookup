import re
import pandas as pd

options = ('s', 'u', 'x')
while True:
    print("*** SELECT OPTION ***")
    print()
    print('s = SEARCH MAC ADDRESS')
    print('u = UPDATE DB FILE')
    print('x = EXIT')
    print()
    user_input = input('Enter an option: ')

    if user_input in options:
        if user_input == 's':
            print()
            m = input('ENTER MAC ADDRESS: ' )
            mc = re.sub('[^A-Fa-f0-9]+', '', m).upper()
            mac = mc[0:6]
            def mac_search(match):
                df = pd.read_csv('oui.db')
                data = df[['Assignment', 'Organization Name']]
                return df.loc[df['Assignment'].eq(match)]
            print('*********** MAC VENDOR ***********')
            print()
            print(mac_search(match=mac))
            print()
            print('***********************************')
        elif user_input == 'u':
            print('OUI database file being updated')
            from oui_db import get_oui_data
            print()
            print('OUI database file has been updated successful')
        elif user_input == 'x':
            exit()
    else:
        print('OPTION NOT AVAILABLE')
        break




