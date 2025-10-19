import feedparser
import json
import time

while True:
    rssFeeds = [
        "https://feeds.npr.org/1001/rss.xml",
        "http://rss.cnn.com/rss/cnn_topstories.rss",
        "http://rssfeeds.usatoday.com/usatoday-NewsTopStories",
        "http://newsrss.bbc.co.uk/rss/newsonline_world_edition/americas/rss.xml"
        "https://feeds.nbcnews.com/nbcnews/public/news",
        "https://abcnews.go.com/abcnews/topstories",
        "https://www.cbsnews.com/latest/rss/main",
        "https://www.politico.com/rss/politicopicks.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
        "https://www.washingtontimes.com/rss/headlines/news",
        "https://www.latimes.com/local/rss2.0.xml",
        "https://thehill.com/resources/rss-feeds/",
        "https://rss.feedspot.com/usa_news_rss_feeds/",
    ]

    for url in rssFeeds:
        feed = feedparser.parse(url)
        for entry in feed.entries:
            if entry.title in tracked_headlines:
                continue
            tracked_headlines.append(entry.title)
            count += 1
            headlines.append(
                {
                    "source": feed.feed.title,
                    "title": entry.title,
                    "link": entry.link,
                    "published": entry.get("published", None),
                }
            )
    with open("headlines.json", "w", encoding="utf-8") as f:
        json.dump(headlines, f, indent=4, ensure_ascii=False)
    print(count)

    time.sleep(60)
