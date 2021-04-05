from returnURL import *
def Main():
    a = raw_input("Enter the URL of a playlist you would like to download the playlist cover for:\n");
    f = returnURL(a);
    print(f.split('<meta property="og:image" content="')[1].split('"')[0]);
    Main();
Main();
