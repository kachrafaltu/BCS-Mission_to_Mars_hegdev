#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


import pandas as pd


# In[3]:


import time


# In[4]:


import pymongo


# In[5]:

# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ## Visit the NASA mars news site

# In[6]:


# Visit the Mars news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=3)


# In[7]:


# Convert the browser html to a soup object
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[8]:


print(news_soup.prettify())
#print(news_soup)
#print(slide_elem)


# In[9]:


news_titles = news_soup.find_all('div', class_='content_title')
for title in news_titles:
    print(title)


# In[10]:


#display the current title content
cur_title = news_soup.find('div', class_='content_title')


# In[11]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title_text = []
for title in news_titles:
    news_title_text.append(title.text)
    print(title.text)


# In[12]:


news_paras = news_soup.find_all('div', class_='article_teaser_body')
news_para_text = []
for news_para in news_paras:
    news_para_text.append(news_para.text)
print(news_para_text)


# In[13]:


# Use the parent element to find the paragraph text



# ## JPL Space Images Featured Image

# In[14]:


image_tags = news_soup.find_all('div',class_='list_image')
img_urls=[]
for image_tag in image_tags:
    print(image_tag.find('img')["src"])
    img_urls.append(image_tag.find('img')["src"])
    
#image_url=image_tag.find('img')["src"]
#img_url
print(img_urls)


# In[15]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)
#time.sleep(1)
html = browser.html
image_soup = soup(html, 'html.parser')


# In[16]:


button_div = image_soup.find('div',class_='floating_text_area')
print(button_div)
button_tag = button_div.find('button',class_= 'btn btn-outline-light')
print(button_tag)


# In[17]:


try:
        browser.links.find_by_partial_text('FULL IMAGE').click()
        print('Navigated to large image')
except:
        print("Scraping Complete")


# In[18]:


html = browser.html
image_soup = soup(html, 'html.parser')
print(image_soup.prettify())


# In[19]:


featured_img = image_soup.find('img', class_='fancybox-image')
print(featured_img)
featured_img_src = featured_img['src']
print(featured_img_src)
absolute_url = url + '/' +  featured_img_src
print(' Absolute_url :' ,absolute_url)
#<a target="_blank" class="showimg fancybox-thumbs" href="image/featured/mars2.jpg"> <button class="btn btn-outline-light"> FULL IMAGE</button></a>


# # Find and click the full image button
# soup = Soup(html, 'html.parser')
# 

# In[20]:


# Parse the resulting html with soup


# # find the relative image url
# 
# img_url_rel

# # Use the base url to create an absolute url
# 
# img_url

# ## Mars Facts

# In[21]:


url = 'https://galaxyfacts-mars.com'
tables = pd.read_html(url)
df = tables[0]
df.rename(index={0: "Description", 1: "Mars", 2:"Earth"})
new_df=df.rename(columns={df.columns[0]: 'Description',df.columns[1]: 'Mars', df.columns[2]: 'Earth'})
new_df.head()


# In[22]:


# Use `pd.read_html` to pull the data from the Mars-Earth Comparison section
# hint use index 0 to find the table

new_df.head()


# In[23]:


mars_facts_html = new_df.to_html()


# ## Hemispheres

# In[24]:


url = 'https://marshemispheres.com/'

browser.visit(url)
html = browser.html
link_soup = soup(html, 'html.parser')

print(link_soup.prettify())


# In[25]:


all_html_links=[]
all_hemis=[]
all_items=link_soup.find_all('div',class_="description")
for item in all_items:
    url_def = item.find('a',class_="itemLink product-item")
    hemis_name=item.find('h3').text
    print(hemis_name)
    print(url+url_def['href'])
    all_html_links.append(url+url_def['href'])
    all_hemis.append(hemis_name)
print(all_html_links)
print(all_hemis)

image_urls=[]
for html_link in all_html_links:
    browser.visit(html_link)
    time.sleep(2)
    html = browser.html
    img_link_soup = soup(html, 'html.parser')
    full_image_refs = img_link_soup.find_all('li')
    full_image = (full_image_refs[0]).find('a')['href']
    print(full_image)
    image_urls.append(url+full_image)
#    for ref in full_image_refs:
#        print(ref)
#        image_ref=ref.find('a')['href']
#        print(image_ref)
#        image_urls.append(url+image_ref)

print(image_urls)


# # This code did not work and gave StaleElementReferenceException
# links = browser.find_by_tag('img[class="thumb"]')
# all_links=[]
# for link in links:
#     all_links.append(link)
# 
# print(all_links)
# time.sleep(2)
# 
# for link in all_links:
#     try:
#         time.sleep(2)
#         link.click()
#         time.sleep(2)
#     except Browser.StaleElementReferenceException:
#         time.sleep(2)
#         link.click()
#     except:
#         print('Not sure what I can do')
#         
# #    sample_image = browser.links.find_by_partial_text('Sample')
# #    sample_image.click()
#     html = browser.html
#     image_link_soup = soup(html, 'html.parser')
#     print(image_link_soup.prettify())
# #<a target="_blank" href="images/cerberus_enhanced.tif">Original</a>    
# 
#     print("----------------------")
#     full_image_refs = image_link_soup.find_all('li')
#     for ref in full_image_refs:
#         print(ref)
#         image_ref=ref.find('a')['href']
#         print(image_ref)
#     
#     
#     print("----------------------")
#     browser.back()
# 

# # Create a list to hold the images and titles.
# hemisphere_image_urls = []
# hemisphere_texts = []
# 
# # Get a list of all of the hemispheres
# links = link_soup.find_all('a',class_='itemLink product-item')
# print(links)
# for link in links:
#     hemisphere_text=link.find('h3')
# #    hemisphere_text.click()
#     print(hemisphere_text.text)
# #    browser.links.find_by_partial_text()
# #    hemisphere_url=link.find()
# 

# for i in range(len(links)):
#     print(links[i])

# # Next, loop through those links, click the link, find the sample anchor, return the href
# for i in range(len(links)):
#     links[i].click()
#     link_html = browser.html
#     # Parse HTML with Beautiful Soup
#     link_soup = soup(html, 'html.parser')
# 
#     print(link_soup.prettify())
#     # We have to find the elements on each loop to avoid a stale element exception
#     
#     
#     # Next, we find the Sample image anchor tag and extract the href
#     
#     
#     # Get Hemisphere title
#     
#     
#     # Append hemisphere object to list
#     
#     
#     # Finally, we navigate backwards
#     browser.back()

# In[26]:


hemisphere_image_urls = []
for i in range(len(all_hemis)):
    dict_rec = {'img_url': image_urls[i], 'title':all_hemis[i]}
    hemisphere_image_urls.append(dict_rec)

hemisphere_image_urls


# browser.windows.current.close()
browser.quit()

# In[28]:


# Setup connection to mongodb
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# Select database and collection to use
db = client.mars_data
db.drop_collection('hemis')
db.hemis.insert_many(hemisphere_image_urls)
print("Data Uploaded!")
mars_data={
    "latest_news_title": news_title_text[0],
    "latest_news_para":  news_para_text[0],
    "featured_image": absolute_url,
    "mars_fact_html": mars_facts_html,
    "hemis_data": hemisphere_image_urls
}
db.drop_collection('mars_basic_data')
db.mars_basic_data.insert_one(mars_data)
# In[ ]:




