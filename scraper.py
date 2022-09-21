# this script scrapes currently broken ice-machines in McDonalds in US States https://mcbroken.com/

import requests
URL:str = 'https://mcbroken.com/'


def make_request(url:str) -> requests.Response:
    response:requests.Response = requests.get(url)
    return response

def main():
    response:requests.Response = make_request(URL)
    if not response.ok:
        print(f'Invalid response status code: {response.status_code}')
        
    

if __name__ == '__main__':
    main()