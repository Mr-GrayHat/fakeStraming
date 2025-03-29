from flask import Flask, render_template, jsonify
import requests
import os  # <-- Añade esta línea
app = Flask(__name__)


YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')  # <-- Modifica esta línea


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/youtube-trends')
def get_trends():
    url = 'https://www.googleapis.com/youtube/v3/videos'
    params = {
        'part': 'snippet',
        'chart': 'mostPopular',
        'videoCategoryId': '10',
        'maxResults': '12',
        'key': YOUTUBE_API_KEY,
        'regionCode': 'US'
    }

    response = requests.get(url, params=params)
    data = response.json()

    trends = []
    for item in data.get('items', []):
        trends.append({
            'title': item['snippet']['title'],
            'video_id': item['id'],
            'thumbnail': item['snippet']['thumbnails']['high']['url'],
            'channel': item['snippet']['channelTitle']
        })

    return jsonify(trends)


if __name__ == '__main__':
    app.run(debug=True)