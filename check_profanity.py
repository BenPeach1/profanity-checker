import urllib.request

def read_text():
    quotes = open("/Users/bpeach/Documents/Udacity/Projects/intro-to-python/profanity-checker/source/profanity-check.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()

    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    query = urllib.request.quote(text_to_check)
    connection =urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+query)
    output = connection.read()
    ##print(output)
    connection.close()

    if b"true" in output:
        print("Slow down buddy, this has some profanity in it!")
    elif b"false" in output:
        print("Carry on my friend, you're profanity free!")
    else:
        print("Houston, we have a problem --- we couldn't read your document")

read_text()
