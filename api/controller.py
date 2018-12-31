import json
import falcon

from youtube_api import youtube_search
from mp3_scraper import getmp3_link


class ClipSong:

    def on_get(self, req, res):

        try:
            song_query = req.get_param('song', '')
            res.status = falcon.HTTP_200

            videos = youtube_search(query=song_query)
            print('Downloading %s..' % videos[0]['title'][:30])
            song_link = getmp3_link(video_id=videos[0]['id'])

            res.body = json.dumps({'status': True,
                                   'data': {'link': song_link, 'title': videos[0]['title']},
                                   'message': 'success'
                                   })
        except Exception as e:
            res.status = falcon.HTTP_400
            res.body = json.dumps({'status': False,
                                   'data': [],
                                   'message': str(e)
                                   })