from os import link
import feedparser
from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen

def get_post_urls(rss=None):
    urls = []    
    if rss is not None:
        blog_feed = feedparser.parse(rss)
        entries = blog_feed.entries
        for entry in entries:
            link = entry.link
            #for link in links:
            urls.append(link)
    return urls;    

def get_all_post_Elements_text(post_urls):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    
    header_selector = '#et-boc > div > div > div > div.et_pb_row.et_pb_row_0_tb_body.et_pb_equal_columns > div.et_pb_column.et_pb_column_3_5.et_pb_column_0_tb_body.et_pb_css_mix_blend_mode_passthrough > div.et_pb_module.et_pb_post_title.et_pb_post_title_0_tb_body.et_pb_bg_layout_light.et_pb_text_align_left > div > h1'
    time_selector = '#et-boc > div > div > div > div.et_pb_row.et_pb_row_0_tb_body.et_pb_equal_columns > div.et_pb_column.et_pb_column_3_5.et_pb_column_0_tb_body.et_pb_css_mix_blend_mode_passthrough > div.rts-article-info > div.rts-article-info__row > span.rts-article-info__date'
    author_selector = '.rts-article-info__authors' 

    all_time_texts = []
    all_header_texts = []
    all_author_texts = []
    
    for url in post_urls:
        print ('Extracting Elements from url: ' + url)
        req = Request(url,headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page, 'html5lib')
       
        headerElement = soup.select_one(header_selector)
        all_header_texts.append(headerElement.text)
        
        timeElement = soup.select_one(time_selector)
        all_time_texts.append(timeElement.text)

        headerElement = soup.select_one(author_selector)
        all_author_texts.append(headerElement.text)
    
    return all_header_texts,  all_time_texts , all_author_texts
        

    
if __name__ == "__main__":
  feed_url = "https://www.reutersagency.com/feed/?taxonomy=best-sectors&post_type=best"
  post_urls = get_post_urls(feed_url)
  all_post_header_text ,all_post_time_text, all_auther_text = get_all_post_Elements_text(post_urls)
 
  all  =[]
  print('All post Elements:')

  for header_text,time_text,auther_text in zip(all_post_header_text ,all_post_time_text,all_auther_text):
      print("Heading:" + header_text)
      print("Time:" + time_text)
      print("auther:" + auther_text)


    
 