import os
from subprocess import Popen, DEVNULL


def mp4_to_gif(mp4_file: str) -> str:
    r"""
    Convert an .mp4 to a .gif with ffmpeg.

    :param mp4_file: Path to an .mp4 file.
    :return: Path to the converted .gif
    """
    path, mp4_name = os.path.split(mp4_file)
    gif = os.path.join(path, f'{os.path.splitext(mp4_name)[0]}.gif')

    ffmpeg = _get_binary()
    # TODO: are these flags enough to make sure it'll render on GitHub and in Slack?
    command = f'{ffmpeg} -i {mp4_file} -vf scale=320:-1:flags=lanczos,fps=10 {gif}'
    with Popen(command.split(' '), stderr=DEVNULL) as p:
        p.wait()
    return gif


def _get_binary(path: str='ffmpeg') -> str:
    r"""
    Logic for finding the ffmpeg binary. Maybe steal from imageio eventually.

    For now, this is pretty much just an attempt at better error messages when ffmpeg isn't installed.

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
