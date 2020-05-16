import time


def slow_text(text, delay: float):
    for char in text:
        time.sleep(delay)
        print(char, end='', flush=True)


message = 'Time to die, maggot!'
slow_text(message, 0.1)
