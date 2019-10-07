import twitter
import json
import sys
import os
from logging import Logger
import pkg_resources

def _get_creds():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'data', 'twitter_creds.json'), 'r') as f:
      creds = json.load(f)
    return creds


def find_video(tweet_url: str, log: Logger) -> str:
    r"""
    Gets the video URL from the Tweet

    :param tweet_url: URL for a tweet with a video.
    :return: URL of the video itself.
    """
    try:
      creds = _get_creds()
      api = twitter.Api(
        consumer_key=creds['consumer_key'],
        access_token_key=creds['access_token_key'],
        consumer_secret=creds['consumer_secret'],
        access_token_secret=creds['access_token_secret']
      )
    except Exception as e:
      log.error(e)
      raise Exception("There was a problem with your twitter creds")
    tweet_id = tweet_url.strip("/").split("/")[-1]

    status = api.GetStatus(tweet_id)
    media = status.media

    try:
      video = media[0].AsDict()
      
      saved_variant = None
      # Default to m3u8, then highest quality mp4
      for variant in video['video_info']['variants']:
        if variant['content_type'] == 'application/x-mpegURL':
          saved_variant = variant
          break
        elif saved_variant == None:
          saved_variant = variant
        elif variant['content_type'] == "video/mp4" and variant['bitrate'] > saved_variant['bitrate']:
          saved_variant = variant

      return saved_variant['url'].split("?")[0] #Remove query string
    except Exception as e:
      raise Exception("There's no video on this Twitter post")