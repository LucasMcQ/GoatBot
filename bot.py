import praw
import praw.models
import config
import time
import random

GIF0  = "[goat](https://giphy.com/gifs/goat-108Y1SMrGePEDC)"
GIF1  = "[goat](https://giphy.com/gifs/tongue-goat-cMso9wDwqSy3e)"
GIF2  = "[goat](https://giphy.com/gifs/zz49TLnbLJdXq)"
GIF3  = "[goat](https://giphy.com/gifs/dog-goat-milk-mkZ78JB74isVO)"
GIF4  = "[goat](https://giphy.com/gifs/goats-tongue-rTfN2FHPPTABy)"
GIF5  = "[goat](https://giphy.com/gifs/cheezburger-see-5K3Vw3jUqwV56)"
GIF6  = "[goat](https://giphy.com/gifs/goat-XKYjR0Hsjh5cs)"
GIF7  = "[goat](https://giphy.com/gifs/goat-homework-ate-6w6TEAATeBik8)"
GIF8  = "[goat](https://giphy.com/gifs/baby-jump-bBF2oqCpqVRwQ)"
GIF9  = "[goat](https://giphy.com/gifs/goat-2XskdWOosyAWPGTMv8A)"
GIF10 = "[goat](https://giphy.com/gifs/ice-goat-XdACBmg3lx6RG)"
GIF11 = "[goat](https://giphy.com/gifs/cheezburger-cute-goats-l8aAwVtd7VPe8)"
GIF12 = "[goat](https://giphy.com/gifs/goat-clever-LSLhspQ1g7dzG)"
GIF13 = "[goat](https://giphy.com/gifs/cheezburger-funny-dog-goats-DiiQyFONn5sL6)"
GIF14 = "[goat](https://giphy.com/gifs/goat-aYcV6BKQVnPMY)"
GIF15 = "[goat](https://giphy.com/gifs/goats-leaves-critters-YIZl9Tk7dGCOI)"
GIF16 = "[goat](https://giphy.com/gifs/how-goat-forgot-FsaiMwHk9V5ss)"
GIF17 = "[goat](https://giphy.com/gifs/food-goat-licking-Nv0oUgtX9412M)"
GIF18 = "[goat](https://giphy.com/gifs/funny-goat-CzHhegH2ZGsPS)"

gif_lst = [GIF0,GIF1,GIF2,GIF3,GIF4,GIF5,GIF6,GIF7,GIF8,GIF9,GIF10,GIF11,GIF12,GIF13,GIF14,GIF15,GIF16,GIF17,GIF18]
msg_lst = [GIF0,GIF1,GIF2,GIF3,GIF4,GIF5,GIF6,GIF7,GIF8,GIF9,GIF10,GIF11,GIF12,GIF13,GIF14,GIF15,GIF16,GIF17,GIF18]

def login():

    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "goat poster v0.2")

    return r


def run(r):
    for comment in r.subreddit('all').comments(limit=100000000000):
        if ("goat" in comment.body) and (len(comment.body.split()) <= 25):
            if (comment.body not in msg_lst):
                    comment.reply(random_goat())
                    print "JUST POSTED!!!"
                    print comment.body
                    msg_lst.append(comment.body)
                    return


def random_goat():
    return random.choice(gif_lst)



r = login()




while True:
    try:
        run(r)
    except:
        print "EXCEPTION"
        time.sleep(50)
