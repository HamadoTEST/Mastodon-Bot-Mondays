from mastodon import Mastodon
import time

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

# Run the post_video function
post_video()
