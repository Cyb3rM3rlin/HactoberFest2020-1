*/ 
<<<<<<HOW TO INSTALL REQUIRED PACKAGES>>
--------------------------------------------------
pip install pytube
Collecting pytube
Downloading https://files.pythonhosted.org/packages/af/56/c9b484e93e1f3a4ef6aefbc1e68258121831007938556daf968ab4519c9c/pytube-9.3.5-py3-none-any.whl
Installing collected packages: pytube
Successfully installed pytube-9.3.5
/*
#importing the youtube
from pytube import YouTube
#to get a link of the video
yt = YouTube('https://www.youtube.com/watch?v=-KnAZcXzxRA')
#pytube API makes all information intuitive to access. For example, this is how you would get the video’s title:
yt.title
#to select the media format
yt.streams.all()
#to get the first stream: FROM VARIOUS RESULTS
stream = yt.streams.first()
>>> stream
<Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2">
#VIDEO DOWNLOAD
stream.download('f:/')
'f:/Redmi Note 7 Fake 48MP Camera Explained \U0001f525\U0001f525\U0001f525.mp4'
stream.download()
'C:\\Python\\Python361\\Redmi Note 7 Fake 48MP Camera Explained \U0001f525\U0001f525\U0001f525.mp4'
