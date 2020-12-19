# Scrape link from site with specific date when published


#### Run this command for first time only 

```sh
$ pip install requirements.txt
```
and update chromedriver.exe according to your Chrome Browser.

now open ``main.py`` and replace "chrome_default_path" variable path according to your browser default path.
```sh
chrome_default_path = r"past your browser default profile path here"
```

#Note: you need python and pip installed on your system.

### How to use
Now enter your user id and date

like this 

```sh
$ python main.py --user_id 27 --date 2020/12/18
```
or 
```sh
$ python main.py --u 27 --d 2020/12/18
```
Then it will show result after sometime like this.

```sh
$ python main.py --user_id 27 --date 2020/12/18

----------------2020/12/18---------------
http://xyz.net/cn/rangeelay-2013-1080p-h264/
http://xyz.net/cn/ramji-londonwaley-2005-1080p-h-264/
http://xyz.net/cn/rajoo-dada-1992-1080p-h264/
http://xyz.net/cn/raj-hath-1956-480p-h264/
http://xyz.net/cn/raat-1992-1080p-h264/
http://xyz.net/cn/raasukutti-1992-352p-mpeg4/
http://xyz.net/cn/qatil-haseeno-ka-2001-1080p-h264/
http://xyz.net/cn/pyare-mohan-2006-1080p-h264/
http://xyz.net/cn/pyar-ki-kahani-1971-480p-h264/
http://xyz.net/cn/pyar-ke-naam-qurbaan-1989-720p-h-264/
http://xyz.net/cn/pyar-diwana-hota-hai-2002-1080p-h-264/
http://xyz.net/cn/pyaar-mein-aisa-hota-hai-2013-1080p-h264/
http://xyz.net/cn/pyaar-diwana-1972-576p-h264/
http://xyz.net/cn/yeh-hai-jalwa-2002-hindi-dvdrip-x264/
-------------------------------------
```


