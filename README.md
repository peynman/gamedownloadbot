# GameDownloadBot
Video game websites scraper

### requirements
* scrapy
* pproxy

### HTTP -> Socks proxy
* ```pproxy -l http://:8181 -r socks5://127.0.0.1:1080```

### Usage
* ```pip install -r requirements.txt```
* ```scrapy crawl (fitgirl, ...)```
