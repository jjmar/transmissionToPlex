from mimetypes import guess_type


def classify_downloaded_content(list_of_files):
    num_movie_files = 0

    for file in list_of_files:
        mimetype = guess_type(file.name)[0]  # e.g 'video/mp4'

        if mimetype and mimetype.split('/')[0] == 'video':
            num_movie_files += 1

    return 'movie' if num_movie_files < 2 else 'tv'
