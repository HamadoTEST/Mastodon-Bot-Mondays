from mastodon import Mastodon
import time
import schedule

# Initialize Mastodon client
mastodon = Mastodon(
    access_token='9_Nn0StX-THA1-wTRstEB9fj-wBKALupNHRNyY_9qGo',
    api_base_url='https://botsin.space'
)

def post_video():
    # Upload video
    media = mastodon.media_post(
        'mondays.mp4',
        mime_type='video/mp4'
    )

    # Wait for file processing to complete
    time.sleep(10)

    # Post status with media
    mastodon.status_post(
        status='Monday Monkey Lives For The Weekend, Sir',
        media_ids=[media['id']]
    )

    print("Video posted successfully!")

# Schedule the post_video function to run every Monday at 10:00 PM
schedule.every().monday.at("22:00").do(post_video)

while True:
    schedule.run_pending()
    time.sleep(1)
