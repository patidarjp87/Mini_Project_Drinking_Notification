import time
from plyer import notification
if __name__=="__main__":
    while 1:
        notification.notify(
            title="It's time to drink water..!",
            message="It's good to drink 4L water everyday..!",
            app_icon=None,
            timeout=10
        )
        time.sleep(60*60)