# Youtube-Transcript-Summarizer
This web application uses the LexRank natural language processing algorithm to extract transcripts from YouTube videos and generate meaningful summaries. It allows users to customize the summary length and download the results for easy access.
# Features
1. Accepts any public YouTube video URL
2. Extracts transcripts using the youtube_transcript_api
3. Generates summaries using the LexRank algorithm (via the Sumy library)
4. Offers multiple summary lengths: Small (10 lines), Medium (20 lines), Large (30 lines)
5. Allows users to download the summary as a .txt file
6. Displays the video thumbnail for better context
7. Includes additional sections such as Login, FAQs, Reviews, and Contact Us
# Functional flow
- The user enters a YouTube video link
- The system extracts the video ID and sends it to the API
- The transcript is retrieved from the video
- The LexRank algorithm processes the transcript based on the selected summary length
- The generated summary is displayed along with the word count and video thumbnail
- The user can download the summary file
