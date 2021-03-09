import time
from plyer import notification

if __name__=="__main__":
    while True:

        notification.notify(
            title="Its Time to Drink water",
            message="Drinking water is very important because it keeps your body active andyour mind refreshed",
            app_icon="/home/abhinav/drinkWater/glass.png.ico",
            timeout=4
    )
    time.sleep(60*60)