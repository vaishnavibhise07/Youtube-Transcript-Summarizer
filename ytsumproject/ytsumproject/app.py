from flask import Flask, render_template, request, send_file
from youtube_transcript_api import YouTubeTranscriptApi
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from io import BytesIO

app = Flask(__name__)

def lexrank_summarizer(text, summary_length):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, summary_length)
    return ' '.join([str(sentence) for sentence in summary])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contactus')
def contact():
    return render_template('contactus.html')

@app.route('/faqs')
def faqs():
    return render_template('faqs.html')

@app.route('/reviews')
def reviews():
    return render_template('reviews.html')

@app.route('/gettranscript')
def gettranscript():
    return render_template('gettranscript.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    youtube_url = request.form['video_url']
    video_id = youtube_url.split('=')[-1]

    try:
        transcript = get_video_transcript(video_id)
        summary_size = request.form['summary_size']
        if summary_size == 'small':
            summary_length = 10
        elif summary_size == 'medium':
            summary_length = 20
        elif summary_size == 'large':
            summary_length = 30
        summary = lexrank_summarizer(transcript, summary_length)
        num_words = len(summary.split())
        video_thumbnail = f'https://img.youtube.com/vi/{video_id}/maxresdefault.jpg'
        return render_template('summary.html', summary=summary, num_words=num_words, video_url=youtube_url, video_thumbnail=video_thumbnail)
    except Exception as e:
        error_message = str(e)
        return render_template('index.html', error=error_message)

@app.route('/download_summary', methods=['POST'])
def download_summary():
    summary = request.form['summary']

    summary_bytes = summary.encode('utf-8')
    return send_file(BytesIO(summary_bytes), as_attachment=True, download_name='summary.txt')

@app.route('/gettranscript')
def get_transcript():
    return render_template('gettranscript.html')

@app.route('/get_transcript', methods=['POST'])
def process_get_transcript():
    youtube_url = request.form['video_url']
    transcript = get_video_transcript(youtube_url)
    return render_template('transcript.html', transcript=transcript)

def get_video_transcript(video_url):
    video_id = video_url.split('=')[-1]
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = ' '.join([line['text'] for line in transcript_list])
    return transcript

if __name__ == '__main__':
    app.run(); 
