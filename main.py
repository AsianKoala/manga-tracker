from mailbox import Maildir
import fire
import json
import requests

class Manga:

    def __init__(self, title='', mal_link='', demographic='', genres=[], score = -1, last_chapter = -1) -> None:
        self.title = title
        self.mal_link = mal_link
        self.demographic = demographic
        self.genres = genres
        self.score = score
        self.last_chapter = last_chapter

    def add_to_json(json):
        print()

    def update_json(json):
        print()

    def remove_from_json(json):
        print()

def update_manga_txt():
    print()

def get_client_id():
    ret = ''
    with open('./id.txt', 'r') as file:
         ret = file.read().strip()
    return ret

def clear_manga():
    with open('./data/tracked_manga.txt', 'r') as file:
        with open('./data/tracked_manga_backup.txt', 'w') as backup_file:
            backup_file.writelines(file.readlines())
    file = open('./data/tracked_manga.txt', 'w')
    file.close()

def get_tracked_manga():
    ret = {}
    with open('./data/tracked_manga.txt', 'r') as file:
        line = file.readline()
        try:
            json.loads(line)
        except ValueError:
            line = '{}'
        ret = json.loads(line)
    return ret

def write_tracked_manga(to_write):
    with open('./data/tracked_manga.txt', 'w') as file:
        file.write(json.dumps(to_write))

def track(manga_name: str):
    """
    Tracks the manga with name "manga_name"
    :param manga_name: the name of the manga
    :return: none
    """
    MAL_HEADER = 'X-MAL-CLIENT-ID'
    header = {MAL_HEADER:get_client_id()}
    limit = 1
    base = 'https://api.myanimelist.net/v2/anime?q='
    query = manga_name.replace(' ', r'%20')
    api = base + query + 'limit=' + str(limit)
    r = requests.get(api, header)
    print(r.content)
    print(get_client_id())

tracked_manga = get_tracked_manga()

def main():
    fire.Fire({
        "track": track
    })

if __name__ == '__main__':
    main()
    