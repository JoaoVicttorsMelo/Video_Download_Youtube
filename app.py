from flask import Flask, render_template, request
import pytube
import traceback
import os
import getpass
import platform
app = Flask(__name__, template_folder='template', static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def getvalue():
    if request.method == 'POST':
        name = request.form['url']
        try:
            url = name
            youtube = pytube.YouTube(url)
            video = youtube.streams.get_highest_resolution()
            so = platform.system()

            if so == 'Windows':
                video_path = r'C:/Users/' + getpass.getuser() + '/Downloads/Youtube_Download/'
                if not os.path.exists(video_path):
                    os.makedirs(video_path)
                    video.download(video_path)

            elif so == 'Linux':
                video_path = r'/home/ubuntu/Desktop/'
                if not os.path.exists(video_path):
                    os.makedirs(video_path)
                    video.download(video_path)


            return render_template('index.html')
        except Exception as e:
            traceback.print_exc(e)
            return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
