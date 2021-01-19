from flask import Flask, render_template, request
import pytube
import getpass
import traceback
import os
app = Flask(__name__, template_folder='template', static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def getvalue():
    name = request.form['url']
    try:
        url = name
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        audio = youtube.streams.get_audio_only()
        video_path = r'C:/Users/' + getpass.getuser() + '/Downloads/Youtube_Download'
        audio_path = r'C:/Users/' + getpass.getuser() + '/Downloads/Youtube_Download/Audio'
        if not os.path.exists(video_path):
            os.makedirs(video_path)
            os.makedirs(audio_path)

        video.download(video_path)
        audio.download(audio_path)

        return render_template('index.html')
    except Exception as e:
        traceback.print_exc(e)
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
