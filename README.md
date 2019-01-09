# SongClipper

SongClipper is an application that extracts audio files from video streaming sites (only YouTube in `v1.0.0`) and downloads the mp3 files.

## Getting started

There are 3 interfaces in the application

* Command line interface

* REST API

* [Frontend with google chrome extension](https://chrome.google.com/webstore/detail/song-clipper/bialkkkbimchmgddmlbbbnlmfcnkfjnb)

### Command line interface

This component can be independently used to search and download audio files.

### Quick start

```
pip install -r requirements.txt
python main.py

```

### REST API

This component is used as backend for frontend chrome extension.

### Quick start

```
pip install -r requirements.txt
python api/app.py

```

### Google chrome extension

An interface for users to search and download audio files.

### Quick start

* Visit `chrome://extensions` in your browser and ensure that the Developer mode checkbox in the top right-hand corner is checked.

* Click Load unpacked extension and select the directory in which your extension files live. If the extension is valid, you will see the details of the
extension as shown in the image along with a new application icon on the address bar.

You can find the published extension [here](https://chrome.google.com/webstore/detail/song-clipper/bialkkkbimchmgddmlbbbnlmfcnkfjnb)

![extension](./extension.png)

# Contributing

You are welcome to submit issues and enhancement requests and work on any of the existing issues. Follow this simple guide to contribute to the repository.

 1. **Create** or pick an existing issue to work on
 2. **Fork** the repo on GitHub
 3. **Clone** the forked project to your own machine
 4. **Commit** changes to your own branch
 5. **Push** your work back up to your forked repo
 6. Submit a **Pull request** from the forked repo to our repo so that we can review your changes

NOTE: Be sure to merge the latest from "upstream" before making a pull request!


