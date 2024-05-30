from django.shortcuts import render
from .models import contents
from .temple import *
import requests,json


def index(request):
    return render(request, 'content/index.html', {'title': "Content"})

def index_photo(request):
    photos = contents.objects.filter(type=MediaType.PHOTO)
    return render(request, 'content/photo.html', {'title': "Photo"})


def get_youtube_video_data(video_id):
    return requests.get(f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key=AIzaSyCPQCHpQ7GcvMRDrvaochinfvx-xD-B8PI")
def index_video(request):
    videos = []
    for video in contents.objects.filter(type=MediaType.VIDEO):
        if video.platformType == PlatformType.YT:
            video_id = video.urlContent.split('v=')[-1]
            video_get_data = requests.get(f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key=AIzaSyCPQCHpQ7GcvMRDrvaochinfvx-xD-B8PI").json()
            author_get_data = requests.get(f"https://www.googleapis.com/youtube/v3/channels?part=snippet&id={video_get_data.items.snippet.channelId}&key=AIzaSyCPQCHpQ7GcvMRDrvaochinfvx-xD-B8PI").json()
            video.videoPreview = f"https://i.ytimg.com/vi/{id}/default.jpg"
            video.authorAvatar = author_get_data.items.snippet.thumbnails.default.url
            video.title = video_get_data.items.snippet.title
            videos.append(video)

    return render(request, 'content/video.html', {'title': "Videos",'videos': videos})



def view_content(request, id):
    return render(request, 'content/view_video.html', {'title': "content", 'video': contents.objects.get(id=id)})