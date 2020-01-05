from google import google
import praw


def query(word):
    dictionary = {}
    response = google.search(word, 1)
    top = response[0]
    if 'wikipedia' in top.link:
        dictionary['w'] = top.link
        dictionary['g'] = response[1].link
    else:
        dictionary['g'] = top.link
        dictionary['w'] = next(result for result in response if 'wikipedia' in result.link).link

    reddit_links = google.search(f'{word} reddit', 1)

    dictionary['r'] = next(result for result in reddit_links if len(result.link.split('/')) == 6).link

    return dictionary

