from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
import os

Gemini_API_KEY = 'AIzaSyAdikxjuj8iMVLN3gAOQ-kUiR5YAM3dCd4'
genai.configure(api_key=os.environ["Gemini_API_KEY"])


#https://youtu.be/zPG4NjIkCjc?si=BhSK7EjvuS9q6C6Q  -- 5min vid
#https://youtu.be/x7X9w_GIm1s?si=U21xhhdsMiS2KdyJ  --2min vid

url = input('pls share the link of the video you want to summarize:')
url= url.split('/')
url = url[3]

transcript = YouTubeTranscriptApi.get_transcript(url)

transcriptText = ''

for i, transcript_item in enumerate(transcript):
    #store the the whole transcript in one variable
    transcriptText += transcript_item["text"] + "\n"
    #print(f'{transcript_item["text"]}')


print('summarizing')
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("summarize the following, in way it is very easy to understand the context."+ transcriptText)
print(response.text)

