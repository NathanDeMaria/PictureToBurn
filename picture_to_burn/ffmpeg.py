import os
import warnings
from subprocess import Popen, DEVNULL


def mp4_to_gif(mp4_file: str, width: int) -> str:
    r"""
    Convert an .mp4 to a .gif with ffmpeg.

    :param mp4_file: Path to/url of an .mp4 file.
    :param width: Width of the output gif in pixels.
    :return: Local path to the converted .gif
    """
    _, mp4_name = os.path.split(mp4_file)
    gif = f'{os.path.splitext(mp4_name)[0]}.gif'
    if os.path.exists(gif):
        raise FileExistsError(gif)

    ffmpeg = _get_binary()
    command = f'{ffmpeg} -i {mp4_file} -vf scale={width}:-2,fps=10 {gif}'
    with Popen(command.split(' '), stderr=DEVNULL) as p:
        p.wait()
    size_mb = os.path.getsize(gif) / 1000000
    if size_mb > 2:
        warnings.warn(f"Gif created is {size_mb:.02f} MB, "
                      f"and might not display in Slack")

    return gif


def _get_binary(path: str = 'ffmpeg') -> str:
    r"""
    Logic for finding the ffmpeg binary. Maybe steal from imageio eventually.

    For now, this is pretty much just an attempt
    at better error messages when ffmpeg isn't installed.

    :param path: path to the ffmpeg binary.
    :return: path to the ffmpeg binary.
    """
    try:
        with Popen(path, stderr=DEVNULL) as p:
            p.wait()
    except FileNotFoundError:
        raise FileNotFoundError(
            f"ffmpeg not found at {path}. "
            f"If you have conda, an easy way to get ffmpeg is "
            f"`conda install ffmpeg -c conda-forge`"
        )
    return path
