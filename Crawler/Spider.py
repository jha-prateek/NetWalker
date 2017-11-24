from urllib2 import *
from bs4 import BeautifulSoup
from robotparser import RobotFileParser
import metadata_parser
from lxml import etree
import requests


class spider(object):
    CurLink = ""
    linkURI = []
    texts = []
    Meta = {}

    def __init__(self, link):
        self.CurLink = link
        self.r = RobotFileParser()

    def crawl(self):
        self.r.set_url(urlparse.unquote(self.CurLink))
        self.r.read()

        self.html = urlopen(self.CurLink).read()
        self.bs = BeautifulSoup(self.html, "lxml")

        for script in self.bs(["script", "style"]):
            script.extract()
        text = self.bs.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        for chunk in chunks:
            if chunk:
                self.texts.append(chunk)

        # site = urlparse.urlsplit(self.CurLink).scheme + "://" + urlparse.urlsplit(self.CurLink).netloc + "/sitemap.aspx"
        # r = requests.get(site)
        if requests.get(urlparse.urlsplit(self.CurLink).scheme + "://" + urlparse.urlsplit(self.CurLink).netloc + "/sitemap.aspx").ok == True:
            root = etree.fromstring(requests.get(urlparse.urlsplit(self.CurLink).scheme + "://" + urlparse.urlsplit(self.CurLink).netloc + "/sitemap.xml").content)
            for sitemap in root:
                children = sitemap.getchildren()
                self.linkURI.append(children[0].text)
        elif requests.get(urlparse.urlsplit(self.CurLink).scheme + "://" + urlparse.urlsplit(self.CurLink).netloc + "/sitemap.xml").ok == True:
            root = etree.fromstring(requests.get(urlparse.urlsplit(self.CurLink).scheme + "://" + urlparse.urlsplit(self.CurLink).netloc + "/sitemap.xml").content)
            for sitemap in root:
                children = sitemap.getchildren()
                self.linkURI.append(children[0].text)
        else:
            for link in self.bs.findAll('a',href=True):
                aLink = urlparse.urljoin(self.CurLink,link['href'])

                if(self.r.can_fetch("*",aLink)):
                    self.linkURI.append(aLink)

        page = metadata_parser.MetadataParser(url=self.CurLink)
        meta = page.metadata

        keyw = "null"
        descr = "null"
        if (meta.get('meta').get('Keywords')):
            keyw = meta['meta']['Keywords'].split(', ')

        if (meta.get('meta').get('Description')):
            descr = meta['meta']['Description']

        self.Meta = {
            'title': meta['page']['title'],
            'url': meta['_internal']['url_actual'],
            'description': descr,
            'keyword': keyw
        }
