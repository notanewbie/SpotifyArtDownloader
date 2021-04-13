import urllib.request


def returnURL(url):
    returned = urllib.request.urlopen(url=url).read()
    return returned


def get_playlist_cover():
    inputted_URL = input("Enter the URL of a playlist you would like to download the playlist cover for:\n")

    caught = str(returnURL(inputted_URL))

    formatted = caught.split('<meta property="og:image" content="')[1].split('"')[0]
    return formatted


if __name__ == '__main__':
    print("\n-----------------\n\n\n" + get_playlist_cover() + "\n\n")

    input("-----------------\n\nPress enter to exit the program.\n")
