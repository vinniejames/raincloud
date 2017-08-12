# RainCloud

SoundCloud backup, download your SoundCloud playlists, liked songs, etc

Step 1: Scroll all the way down to the end of your user page, eg https://soundcloud.com/vinnie_dplm

Step 2: Copy and paste the code below into your console
```
(function(){
  var nodes = document.getElementsByClassName('soundTitle__title');
  var rainCloud = [];

  Array.prototype.forEach.call(nodes, function(el) {
      rainCloud.push(el.href);
  });

  copy(rainCloud);
  console.log(rainCloud, 'xx');
})();
```
Step 3: Your playlist is now in your clipboard, copy it into playlist.py, eg

```
songs = [paste here]
```
Alternately, you may add a comma separated list of user names, which will download the entirety of each users tracks, eg
```
songs = ["https://soundcloud.com/vinnie_dplm", "https://soundcloud.com/dante-gbrl", "https://soundcloud.com/julychilduk"]
```

Step 4: Install [youtube-dl](https://rg3.github.io/youtube-dl/download.html) (`brew install youtube-dl`), and [ffmpeg](http://www.ffmpegmac.net/) (`brew install ffmpeg`) 

Step 5: Open up Terminal, navigate to this repo, run `python raincloud.py`

Step 6: Enjoy your music FOREVER :D
