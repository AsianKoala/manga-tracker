import json

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

def process_request(request):
    print()
