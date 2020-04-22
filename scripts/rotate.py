from browser import document, html

box = document['rotate-box']
angle = 10


def change(e):
    global angle
    box.style.transform = f"rotate({angle}deg)"
    angle += 10


document['rotate-btn'].bind('click', change)
