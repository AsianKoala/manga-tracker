import requests
from manga import Manga
from backend import *

def track(manga_name: str):
    MAL_HEADER = 'X-MAL-CLIENT-ID'
    header = {MAL_HEADER:get_client_id()}
    limit = 1
    base = 'https://api.myanimelist.net/v2/anime?q='
    query = manga_name.replace(' ', r'%20')
    api = base + query + 'limit=' + str(limit)
    r = requests.get(api, header)
    process_request(r)

def test_mal_api():
    api = 'https://myanimelist.net/apiconfig/references/api/v2#tag/user-animelist'
    r = requests.get(api)
    print(r.content)

tracked_manga = get_tracked_manga()

def main():
    pass

if __name__ == '__main__':
    main()
    