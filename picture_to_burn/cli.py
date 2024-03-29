import os
import warnings
from fire import Fire

from picture_to_burn import mp4_to_gif, find_mp4


def convert(some_mp4: str, width: int = 320):
    """
    Convert something to a gif. Currently supports local .mp4 files and tweets.
    """
    if os.path.isfile(some_mp4) or _is_ffmpegable_url(some_mp4):
        pass
    elif 'twitter.com' in some_mp4:
        some_mp4 = find_mp4(some_mp4)
    else:
        raise NotImplementedError(
            f"Can't find a way to convert {some_mp4} into a gif")
    gif = mp4_to_gif(some_mp4, width)

    size_mb = os.path.getsize(gif) / 1000000
    if size_mb > 2:
        warnings.warn(f"Gif created is {size_mb:.02f} MB, "
                      f"and might not display in Slack. Making a smaller one.")
        os.remove(gif)
        gif = mp4_to_gif(some_mp4, width // 2)

    print(f"Created gif: {gif}")


# At least, I've tried it with these
FFMPEGABLE = ['ts', 'mp4', 'm3u8']

def _is_ffmpegable_url(s: str) -> bool:
    if not s.startswith('http'):
        return False
    ext = s.split('.')[-1]
    return ext in FFMPEGABLE


def main():
    Fire(convert)


if __name__ == '__main__':
    main()
