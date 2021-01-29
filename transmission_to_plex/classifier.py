from mimetypes import guess_type
from enum import Enum


class MediaType(Enum):
    MOVIE = 1
    TV = 2


def classify_downloaded_content(list_of_files):
    num_video_files = 0

    for file in list_of_files:
        mimetype = guess_type(file.name)[0]  # e.g 'video/mp4'

        if mimetype and mimetype.split('/')[0] == 'video':
            num_video_files += 1

    return MediaType.MOVIE if num_video_files < 2 else MediaType.TV
