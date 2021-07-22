import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "Hello Bhai Work Hard for Life Mate",
            timeout = 10
        )
        time.sleep(20)