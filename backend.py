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

if __name__ == '__main__':
    BLOCKCHAR = '#'
    width = 10
    xw = BLOCKCHAR * (width+3)
    xword = 'bruhwtf'
    xw += (BLOCKCHAR*2).join([xword[p:p+width] for p in range(0, len(xword), width)])
    xw += BLOCKCHAR*(width+3)
    print(xw)
