import sys
reload(sys)
sys.setdefaultencoding('UTF8')

import opml
from alphabet_detector import AlphabetDetector
ad = AlphabetDetector()

def write_markdown(feeds):
	with open("output.md", "w") as f:
		f.write("count = {}".format(len(feeds)))
		for item in feeds:
			f.writelines("\n* %s\n%s" % (item.get("title"), item.get("htmlUrl")))

def filter(outline):
	sections = []

	for section in outline:
			for feed in section:
				if ad.is_latin(feed.text.decode('utf-8')):
					sections.append(feed)
	return sections


def main():
	with open("Subscriptions.opml", "r") as f:
		outline = filter(opml.parse(f))
		feeds = []

		for feed in outline:
			feeds.append({"title": feed.text, "htmlUrl": feed.htmlUrl})
		write_markdown(feeds)


if __name__ == '__main__':
	main()