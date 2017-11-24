
# Dependencies
- Python 2.7
- BeautifulSoup
- MongoDB Client
- RobotParser
- urllib2
- metadata_parser
- requests
- Flask
- lxml
- SK-Learn
- NLTK

# Overview
A Domain based Web Search Engine made using the fusion of various Technologies. It works by taking the query from user 
and feeds it into the NLP module to extract chunks of words that is searched in pre-crawled Database formed using Beautiful Soup and MongoDB.
The chunk is first iterated over the Tf-Idf Dictionary to narrow down the search and hence reducing the overall fetch-time.
