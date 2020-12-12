# imports
from instapy import InstaPy
from instapy import smart_run
import schedule
import time
import logging

# login credentials
insta_username = 'komunitasmakan'
insta_password = 'MaKaN123'

comments = ['Keren @{}',
        'Keren fotonya @{}',
        'Feed lu bagus banget :thumbsup:',
        'Mantap Jiwa :open_mouth:',
        'Make kamera apa nih? @{}?',
        'Mantep @{}',
        'Keliatan enak @{}',
        'Hebat @{}',
        ':raised_hands: Yes!',
        'Keren banget @{} :muscle:',
        'Ah mantap :thumbsup:'
        ]

def job():
    # get an InstaPy session!
    # set headless_browser=True to run InstaPy in the background
    session = InstaPy(username=insta_username,
                    password=insta_password,
                    headless_browser=True,
                    page_delay=25)

    with smart_run(session):
    """ Activity flow """		
    # general settings		
    session.set_dont_include(["friend1", "friend2", "friend3"])		
    
    # activity
    session.set_do_comment(enabled=True, percentage=35)
    session.set_comments(comments)
    session.set_do_follow(enabled=True,percentage=50,times=10)		
    session.like_by_tags(["makan", "makananjogja", "sukamakan", "food", "makananindonesia",
                            "makansehat", "kuliner", "maknyus"], amount=10)

    # Joining Engagement Pods
    session.set_do_comment(enabled=True, percentage=35)
    session.set_comments(comments)
    session.set_do_follow(enabled=True,percentage=40,times=10)
    session.join_pods(topic='food', engagement_mode='no_comments')

schedule.every().day.at("08:33").do(job)
schedule.every().day.at("18:12").do(job)

if __name__ == '__main__':
    logging.warning("Log app started")
    while True:
        logging.warning("slee 10")
        schedule.run_pending()
        time.sleep(10)
