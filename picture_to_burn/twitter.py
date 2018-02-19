import requests
from lxml.html import fromstring

from .ffmpeg import mp4_to_gif


def convert_tweet(tweet_url: str) -> None:
    tweet_mp4 = find_mp4(tweet_url)
    downloaded = download_mp4(tweet_mp4)
    mp4_to_gif(downloaded)


def find_mp4(tweet_url: str) -> str:
    r"""
    Scrape the .mp4 URL out of a tweet link.

    :param tweet_url: URL for a tweet with a video.
    :return: URL of the mp4 itself.
    """
    # TODO: error nicely if the tweet isn't found
    tweet_html = requests.get(tweet_url)

    # TODO: error nicely if there's some kind of parsing error
    tree = fromstring(tweet_html)
    video_div = tree.cssselect('.PlayableMedia-player')[0]
    player_style = video_div.attrib['style'].split('/')[-1]
    media_id = player_style.split('.')[0]
    return f'https://video.twimg.com/tweet_video/{media_id}.mp4'


def download_mp4(mp4_url: str) -> str:
    r"""
    Download an .mp4 file given a URL to the current working directory.

    :param mp4_url: URL of an .mp4 file.
    :return: local file path of that .mp4
    """
    _, mp4_name = mp4_url.split('/')[-1]
    with open(mp4_name, 'wb+') as mp4_file:
        response = requests.get(mp4_url)
        mp4_file.write(response.content)
    return mp4_file
