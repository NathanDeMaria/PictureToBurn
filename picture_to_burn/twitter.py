import requests
from lxml.html import fromstring


def find_mp4(tweet_url: str) -> str:
    r"""
    Scrape the .mp4 URL out of a tweet link.

    :param tweet_url: URL for a tweet with a video.
    :return: URL of the mp4 itself.
    """
    # TODO: error nicely if the tweet isn't found
    tweet_html = requests.get(tweet_url)

    # TODO: error nicely if there's some kind of parsing error
    tree = fromstring(tweet_html.content)
    video_div = tree.cssselect('.PlayableMedia-player')[0]
    player_style = video_div.attrib['style'].split('/')[-1]
    media_id = player_style.split('.')[0]
    return f'https://video.twimg.com/tweet_video/{media_id}.mp4'
