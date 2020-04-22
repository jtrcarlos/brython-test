from browser import document, console, alert


def show(e):
    console.log("Hello")


document['alert-btn'].bind('click', show)
