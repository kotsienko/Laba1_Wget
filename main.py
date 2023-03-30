import requests
import threading
import time
import sys
import click
n = 0


def download(url=""):
    name = url.split("/")[-1]
    global n
    response = requests.get(url=url, stream=True)
    with open(str(name), mode='wb') as file:
        for i in response.iter_content(chunk_size=256):
            if i:
                n += 256
                file.write(i)
    print(f"Successfully uploaded {n} bytes")


def check_bytes():
    while True:
        time.sleep(1)
        print(f"Loaded: |{n}| bytes")
        sys.stdout.flush()


@click.command()
@click.argument("url")
def main(url):
    thread1 = threading.Thread(target=download, args=(str(url),))
    thread2 = threading.Thread(target=check_bytes, daemon=True)
    thread1.start()
    thread2.start()


if __name__ == '__main__':
    main()
