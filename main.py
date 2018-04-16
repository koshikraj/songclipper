from mp3_scraper import getmp3_link, download_mp3
from youtube_api import youtube_search
from youtube_api import HttpError

if __name__ == '__main__':
    """main program which integrate youtube results and song scraper"""

    try:
        videos = youtube_search(query="bom diggy original")
        print(videos)
        download_mp3(url=getmp3_link(video_id=videos[0]['id']), file_name=videos[0]['title'])

    except HttpError as e:
        print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))