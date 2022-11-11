import requests

file_list = requests.get("https://api.github.com/repos/python/cpython/contents/Modules/_sqlite")

for file_ in file_list.json():
    name = file_['name']
    print("Handling %s" % (name,))
    dl_url = file_['download_url']
    with open(name, 'w') as fh:
        resp = requests.get(dl_url)
        resp.raise_for_status()
        fh.write(resp.text)
