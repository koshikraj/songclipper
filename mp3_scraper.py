import re
import requests
import shutil
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

def getmp3_link(video_id, attempts=5):

    while attempts:

        try:
            payload ={"mediaurl": "https://www.youtube.com/watch?v=" + video_id}
            check_resp = requests.post(url="https://www.clipconverter.cc/check.php", data=payload).json()
            print(check_resp)
            payload ={"mediaurl": payload["mediaurl"],
                      "url": check_resp["url"][1]["url"],
                      "filename":check_resp["filename"],
                      "filetype":"MP3",
                      "format":"MP3",
                      "autocheckbox": 1,
                      "audiovol": 0,
                      "audiochannel": 2,
                      "audiobr": 256,
                      "videobr": 224,
                      "videores": "352x288",
                      "customres": "320x240",
                      "timefrom-start": 1,
                      "timeto-end": 1,
                      "id3-artist": "koshik+raj",
                      "id3-title": check_resp["filename"],
                      "id3-album": "ClipConverter.cc",
                      "auto": 1,
                      "image": "https%3A%2F%2Fi.ytimg.com%2Fvi%2F_WW_jdmra7s%2Fmqdefault.jpg",
                      "org-filename": check_resp["filename"],
                      "videoid": check_resp["videoid"],
                      "pattern": "_WW_jdmra7s",
                      "server": "srv91",
                      "serverinterface": "eth0",
                      "service": "YouTube",
                      "lang": "en",
                      "client_urlmap": None,
                      "ipv6": False,
                      "ablock": 1,
                      "clientside": 1,
                      "addon_page": None,
                      "verify": check_resp["verify"]}

            check__post_resp = requests.post(url="https://www.clipconverter.cc/check.php", data=payload).json()

            if check__post_resp.get("hash"):
                download_link = "https://www.clipconverter.cc/download/" + check__post_resp["hash"] + "/" + str(check_resp["videoid"]) + "/"
            else:
                download_link = "https://www.clipconverter.cc" + check__post_resp["redirect"]

            download_resp = requests.get(download_link)
            m = re.findall('location.href="(.*)";', download_resp.text)
            return m[0]
            break

        except Exception as e:
            print(str(e))
            attempts -= 1


def download_mp3(url, file_name, attempts=5):

    print(url)
    while attempts:

        try:
            file_response = requests.get(url=url, stream=True)
            if file_response.status_code == 200:
                with open(dir_path + '/downloads/{}'.format(file_name), 'wb') as f:
                    file_response.raw.decode_content = True
                    shutil.copyfileobj(file_response.raw, f)
            break

        except Exception as e:
            print(str(e))
            attempts -= 1
