import requests

print('Welcome to Site Checker 1.0!')
while True:
    sites = input('Enter the URLs of the sites you want to check (separated by commas): ')
    separated_urls = sites.split(',')

    for site in separated_urls:
        try:
            site = site.strip()
            if '.' not in site:
                print(f'{site} Invalid URL')
                continue

            if not site.startswith('http://') and not site.startswith('https://'):
                site = f'https://{site}'
            response = requests.get(site)

            if response.status_code == 200:
                print(f'{site.lower()} Site is online!')
            else:
                print(f'{site.lower()} Site is offline')
        except requests.exceptions.ConnectionError:
            print('Connection error')

    final = input('Do you need to check another site? y/n ')
    if final.lower() not in ['y', 'n']:
        print('Invalid option')
    elif final.lower() == 'n':
        print('Program terminated!')
        break
