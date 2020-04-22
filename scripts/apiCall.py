from browser import document, ajax, console

url = 'https://api.chucknorris.io/jokes/random'


def on_complete(req):
    import json
    data = json.loads(req.responseText)
    document['norris'].text = data['value']


def get_norris_joke(e):
    req = ajax.ajax()
    req.open('GET', url, True)
    req.bind('complete', on_complete)
    document['norris'].text = 'Loading.....'
    req.send()


document['norris-btn'].bind('click', get_norris_joke)
