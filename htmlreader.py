import urllib.request
import datetime

url_index = {}
TIMEOUT_SECONDS = 10


class CacheEntry:
    def __init__(self, url, data):
        self.url = url
        self.data = data
        self.timestamp = datetime.datetime.now().timestamp()


while True:
    url = input("Enter a URL: ")

    if url.lower() == "exit":
        break

    needs_refresh = False

    if url not in url_index:
        needs_refresh = True
    else:
        cur_time = datetime.datetime.now().timestamp()
        diff_time = cur_time - url_index[url].timestamp

        # if diff_time > TIMEOUT_SECONDS:
        #     needs_refresh = True
        needs_refresh = diff_time > TIMEOUT_SECONDS

    if needs_refresh:
        resp = urllib.request.urlopen(url)
        data = resp.read()
        url_index[url] = CacheEntry(url, data)

    print(url_index[url].data[:60])
