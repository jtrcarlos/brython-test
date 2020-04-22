from browser import document, html, window, console

storage = window.localStorage

if storage.getItem('item'):
    document['item'] <= storage.getItem('item')


def show_item():
    if storage.getItem('item'):
        document['current-item'].text = 'Current item: ' + \
            storage.getItem('item')
    else:
        document['current-item'].text = 'No item'


def add_item(e):
    item = document['item-input'].value
    storage.setItem('item', item)
    show_item()


def remove_item(e):
    storage.removeItem('item')
    document['item'].textContent = ''
    show_item()


document['add-btn'].bind('click', add_item)
document['remove-btn'].bind('click', remove_item)
