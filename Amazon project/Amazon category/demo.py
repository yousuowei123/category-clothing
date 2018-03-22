# -*- coding:utf-8 -*-
# -*- author:cto_b -*-

import requests
from bs4 import BeautifulSoup
import re
from pyquery import PyQuery as pq


filename = '''
<html>
 <head></head>
 <body>
  <div class="a-column a-span3 fsdColumn fsdColumn_3">
   <div class="fsdDeptBox">
    <img alt="" aria-hidden="true" class="fsdDeptFullImage" data-a-hires="https://images-na.ssl-images-amazon.com/images/G/01/gno/SiteDirectory/SD_AV_2x._CB274381403_.png" height="100%" role="presentation" src="https://images-na.ssl-images-amazon.com/images/G/01/gno/SiteDirectory/SD_AV_1x._CB274380261_.png" width="100%" />
    <h2 class="fsdDeptTitle">Prime Video</h2>
    <div class="fsdDeptCol">
     <a class="a-link-normal fsdLink fsdDeptLink" href="/Amazon-Video/s/browse/ref=sd_allcat_aiv/145-2654160-1553056?_encoding=UTF8&amp;node=2858778011" title="All TV shows, movies, and more">All Videos</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/Prime-Video/s/browse/ref=sd_allcat_aiv_piv/145-2654160-1553056?_encoding=UTF8&amp;node=2676882011" title="Prime Originals, exclusives, and more">Included with Prime</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/s/browse/ref=sd_allcat_nav_sa_aos/145-2654160-1553056?_encoding=UTF8&amp;filterId=OFFER_FILTER%3DSUBSCRIPTIONS&amp;node=2858778011" title="HBO, SHOWTIME, STARZ, and more">Amazon Channels</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/rent-or-buy-amazon-video/b/ref=sd_allcat_aiv_shop/145-2654160-1553056?ie=UTF8&amp;node=7589478011" title="New releases, latest seasons, and more">Rent or Buy</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/gp/video/watchlist/ref=sd_allcat_aiv_wlst/145-2654160-1553056">Your Watchlist</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/gp/video/library/ref=sd_allcat_aiv_yvl/145-2654160-1553056">Your Video Library</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/gp/feature.html/ref=sd_allcat_aiv_wtv/145-2654160-1553056?ie=UTF8&amp;docId=1001423601">Watch Anywhere</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/gp/video/getstarted/ref=sd_allcat_aiv_gs/145-2654160-1553056">Getting Started</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="#">More to Explore</a>
    </div>
   </div>
   <div class="fsdDeptBox">
    <img alt="" aria-hidden="true" class="fsdDeptFullImage" data-a-hires="https://images-na.ssl-images-amazon.com/images/G/01/gno/SiteDirectory/SD_music_2x._CB274422802_.png" height="100%" role="presentation" src="https://images-na.ssl-images-amazon.com/images/G/01/gno/SiteDirectory/SD_music_1x._CB274422803_.png" width="100%" />
    <h2 class="fsdDeptTitle">Amazon Music</h2>
    <div class="fsdDeptCol">
     <a class="a-link-normal fsdLink fsdDeptLink" href="/gp/dmusic/promotions/AmazonMusicUnlimited/ref=sd_allcat_dm_hf/145-2654160-1553056" title="Stream tens of millions of songs with weekly new releases">Amazon Music Unlimited</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/gp/dmusic/promotions/PrimeMusic/ref=sd_allcat_dm_pm/145-2654160-1553056" title="Prime members can stream a growing selection of 2 million songs - all ad-free">Prime Music</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/gp/dmusic/mp3/player/ref=sd_allcat_dm_webplayer/145-2654160-1553056" title="music.amazon.com">Open Web Player</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/music-rock-classical-pop-jazz/b/ref=sd_allcat_dm_cds_vinyl/145-2654160-1553056?ie=UTF8&amp;node=5174" title="Purchase millions of albums and vinyl records">CDs &amp; Vinyl</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/MP3-Music-Download/b/ref=sd_allcat_dm_store_hf/145-2654160-1553056?ie=UTF8&amp;node=163856011" title="Buy albums and songs">Download Store</a>
    </div>
   </div>
   <div class="fsdDeptBox">
    <img alt="" aria-hidden="true" class="fsdDeptFullImage" data-a-hires="https://images-na.ssl-images-amazon.com/images/G/01/gno/SiteDirectory/SD_appstore_2x.png" height="100%" role="presentation" src="https://images-na.ssl-images-amazon.com/images/G/01/gno/SiteDirectory/SD_appstore_1x._CB274380261_.png" width="100%" />
    <h2 class="fsdDeptTitle">Appstore for Android</h2>
    <div class="fsdDeptCol">
     <a class="a-link-normal fsdLink fsdDeptLink" href="/b/ref=sd_allcat_adr_banjo/145-2654160-1553056?ie=UTF8&amp;node=11350978011" title="&lt;strong&gt;Actually Free&lt;/strong&gt; apps from Amazon">Underground Apps &amp; Games</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/mobile-apps/b/ref=sd_allcat_adr_app/145-2654160-1553056?ie=UTF8&amp;node=2350149011" title="Shop over 800,000 apps and games">All Apps and Games </a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/Games/b/ref=sd_allcat_adr_gam/145-2654160-1553056?ie=UTF8&amp;node=9209902011" title="Shop new, bestselling, and free games">Games</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/coins/ref=sd_allcat_adr_coins/145-2654160-1553056" title="Spend Less, Play More">Amazon Coins</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/gp/feature.html/ref=sd_allcat_adr_dl/145-2654160-1553056?ie=UTF8&amp;docId=1003016361" title="Install on your Android phone">Download Amazon Appstore</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/gp/feature.html/ref=sd_allcat_adr_amz/145-2654160-1553056?ie=UTF8&amp;docId=1000645111" title="Kindle, Shopping, MP3, IMDb, and more">Amazon Apps</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/gp/mas/your-account/myapps/ref=sd_allcat_adr_yad/145-2654160-1553056" title="View your apps and manage your devices">Your Apps and Devices</a>
    </div>
   </div>
   <div class="fsdDeptBox">
    <img alt="" aria-hidden="true" class="fsdDeptFullImage" data-a-hires="https://images-na.ssl-images-amazon.com/images/G/01/gno/SiteDirectory/SD_clouddrive_2x._CB274420311_.png" height="100%" role="presentation" src="https://images-na.ssl-images-amazon.com/images/G/01/gno/SiteDirectory/SD_clouddrive_1x._CB274420308_.png" width="100%" />
    <h2 class="fsdDeptTitle">Prime Photos and Prints</h2>
    <div class="fsdDeptCol">
     <a class="a-link-normal fsdLink fsdDeptLink" href="/photos/home/ref=sd_allcat_gw_prime_learn/145-2654160-1553056" title="Free unlimited photo storage with Prime">Prime Photos</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/photos/apps/ref=sd_allcat_gw_photos_apps/145-2654160-1553056" title="Download the desktop and mobile apps to access your content anywhere">Get the apps</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/photos/ref=sd_allcat_gw_photos_login/145-2654160-1553056?_encoding=UTF8&amp;sf=1" title="View and upload your photos">Sign in</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/STRING-subnav_primephotos_amazondrive/b/ref=sd_allcat_gw_dr_about/145-2654160-1553056?ie=UTF8&amp;node=15547130011" title="Sync your files, videos, and photos from your desktop. Prime members receive 5 GB free storage.">Amazon Drive</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/gp/drive/download-apps/ref=sd_allcat_gw_dl_apps/145-2654160-1553056" title="Download the desktop and mobile apps to access your content anywhere">Get the apps</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/clouddrive/ref=sd_allcat_gw_drive_login/145-2654160-1553056?_encoding=UTF8&amp;sf=1" title="View and upload your files">Sign in</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/STRING-subnav-prime-photos/b/ref=sd_allcat_gw_print_about/145-2654160-1553056?ie=UTF8&amp;node=14866317011" title="Free delivery with Prime">Online photo printing</a>
    </div>
   </div>
   <div class="fsdDeptBox">
    <img alt="" aria-hidden="true" class="fsdDeptFullImage" data-a-hires="https://images-na.ssl-images-amazon.com/images/G/01/gno/SiteDirectory/SD_kindle_2x._CB274422802_.png" height="100%" role="presentation" src="https://images-na.ssl-images-amazon.com/images/G/01/gno/SiteDirectory/SD_kindle_1x._CB274422803_.png" width="100%" />
    <h2 class="fsdDeptTitle">Kindle E-readers &amp; Books</h2>
    <div class="fsdDeptCol">
     <a class="a-link-normal fsdLink fsdDeptLink" href="/dp/B00ZV9PXP2/ref=sd_allcat_k_ods_eink_bn/145-2654160-1553056" title="Small, light, and perfect for reading">Kindle</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/dp/B00OQVZDJM/ref=sd_allcat_k_ods_eink_mt/145-2654160-1553056" title="Our best-selling Kindle—now even better">Kindle Paperwhite</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/dp/B00IOY8XWQ/ref=sd_allcat_k_ods_eink_ie/145-2654160-1553056" title="Passionately crafted for readers">Kindle Voyage</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/dp/B06XD5YCKX/ref=sd_allcat_k_ods_eink_wy/145-2654160-1553056" title="Now Waterproof">All-New Kindle Oasis</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/dp/B01KMSKNGU/ref=sd_allcat_k_ods_eink_keb/145-2654160-1553056" title="It's not screen time - it's book time">Kindle for Kids Bundle</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/Kindle-Accessories-Electronics/b/ref=sd_allcat_ods_eink_acc/145-2654160-1553056?ie=UTF8&amp;node=370783011" title="Covers, chargers, sleeves and more">Accessories</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/Amazon-Kindle-Ereader-Family/b/ref=sd_allcat_ods_eink_catp/145-2654160-1553056?ie=UTF8&amp;node=6669702011" title="Compare e-readers, find deals, and more">See all Kindle E-Readers</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/Kindle-eBooks/b/ref=sd_allcat_ods_eink_con_books/145-2654160-1553056?ie=UTF8&amp;node=1286228011">Kindle Books</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/Magazines-Journals-Kindle/b/ref=sd_allcat_ods_eink_con_news/145-2654160-1553056?ie=UTF8&amp;node=241646011">Newsstand</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/gp/kindle/ku/sign-up/ui/rw/about/ref=sd_allcat_ods_eink_con_ku/145-2654160-1553056" title="Unlimited reading &amp; listening">Kindle Unlimited</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/kindle-dbs/fd/prime-pr/ref=sd_allcat_ods_eink_con_pr/145-2654160-1553056">Prime Reading</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/gp/feature.html/ref=sd_allcat_ods_eink_con_karl/145-2654160-1553056?ie=UTF8&amp;docId=1000493771" title="For PC, iPad, iPhone, Android, and more">Free Kindle Reading Apps</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="https://www.amazon.com:443/gp/redirect.html/ref=sd_allcat_ods_eink_con_kcr/145-2654160-1553056?location=https://read.amazon.com/&amp;token=4A20D4CA0ECAC5525B84547087B2D7AB202FF134&amp;source=standards" title="Read your Kindle books in a browser">Kindle Cloud Reader</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/gp/digital/fiona/manage/ref=sd_allcat_ods_eink_con_myk/145-2654160-1553056">Manage Your Content and Devices</a>
    </div>
   </div>
   <div class="fsdDeptBox">
    <img alt="" aria-hidden="true" class="fsdDeptFullImage" data-a-hires="https://images-na.ssl-images-amazon.com/images/G/01/gno/SiteDirectory/SD_firetablets_2x._CB274420308_.png" height="100%" role="presentation" src="https://images-na.ssl-images-amazon.com/images/G/01/gno/SiteDirectory/SD_firetablets_1x._CB274420309_.png" width="100%" />
    <h2 class="fsdDeptTitle">Fire Tablets</h2>
    <div class="fsdDeptCol">
     <a class="a-link-normal fsdLink fsdDeptLink" href="/dp/B01GEW27DA/ref=sd_allcat_k_ods_tab_an/145-2654160-1553056" title="Our best-selling Fire tablet—now even better">Fire 7 </a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/dp/B01J94SWWU/ref=sd_allcat_k_ods_tab_ds/145-2654160-1553056" title="Up to 12 hours of battery. Vibrant HD display. Fast performance.">Fire HD 8</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/dp/B01J6RPGKG/ref=sd_allcat_k_ods_tab_sz/145-2654160-1553056" title="1080p Full HD. 32 GB storage. Now with Alexa hands-free.">All-New Fire HD 10</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/dp/B01J90MSDS/ref=sd_allcat_k_ods_tab_afk/145-2654160-1553056" title="If they break it, return it and we’ll replace it. No questions asked.">Fire 7 Kids Edition</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/dp/B01J94SBEY/ref=sd_allcat_k_ods_tab_dfk/145-2654160-1553056" title="Up to 12 hours of battery. 2X the storage. 8” HD display.
Our best kids’ tablet ever.">Fire HD 8 Kids Edition</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/Kindle-Accessories-Electronics/b/ref=sd_allcat_ods_tab_acc/145-2654160-1553056?ie=UTF8&amp;node=370783011" title="Cases, chargers, sleeves and more">Accessories</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/Amazon-Fire-Tablet-Family/b/ref=sd_allcat_ods_tab_catp/145-2654160-1553056?ie=UTF8&amp;node=6669703011" title="Compare tablets, find deals, and more">See all Fire tablets</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/Instant-Video/s/browse/ref=sd_allcat_ods_tab_con_aiv/145-2654160-1553056?_encoding=UTF8&amp;node=2858778011">Prime Video</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/Fire-Tablet-Apps/b/ref=sd_allcat_ods_tab_con_apps/145-2654160-1553056?ie=UTF8&amp;node=3427287011">Apps &amp; Games</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/MP3-Music-Download/b/ref=sd_allcat_ods_tab_con_music/145-2654160-1553056?ie=UTF8&amp;node=163856011">Digital Music</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/Kindle-eBooks/b/ref=sd_allcat_ods_tab_con_books/145-2654160-1553056?ie=UTF8&amp;node=154606011">Kindle Books</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/gp/kindle/ku/sign-up/ui/rw/about/ref=sd_allcat_ods_tab_con_ku/145-2654160-1553056">Kindle Unlimited</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/dp/B01I499BNA/ref=sd_allcat_ods_tab_gno_ftu/145-2654160-1553056">Amazon FreeTime Unlimited</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/gp/digital/fiona/redirect/newsstand/home/ref=sd_allcat_ods_tab_con_news/145-2654160-1553056">Newsstand</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/gp/digital/fiona/manage/ref=sd_allcat_ods_tab_con_myf/145-2654160-1553056">Manage Your Content and Devices</a>
    </div>
   </div>
   <div class="fsdDeptBox">
    <img alt="" aria-hidden="true" class="fsdDeptFullImage" data-a-hires="https://images-na.ssl-images-amazon.com/images/G/01/gno/SiteDirectory/SD_swa_2x._CB529389250_.png" height="100%" role="presentation" src="https://images-na.ssl-images-amazon.com/images/G/01/gno/SiteDirectory/SD_swa_1x._CB529388988_.png" width="100%" />
    <h2 class="fsdDeptTitle">Subscribe with Amazon</h2>
    <div class="fsdDeptCol">
     <a class="a-link-normal fsdLink fsdDeptLink" href="/b/ref=sd_allcat/145-2654160-1553056?ie=UTF8&amp;node=14498690011">All Subscriptions</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/Lifestyle-Home-Hobby-Subscription-Services/b/ref=sd_allcat/145-2654160-1553056?ie=UTF8&amp;node=14498700011">Lifestyle, Home &amp; Hobbies</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/News-Magazine-Subscription-Services/b/ref=sd_allcat/145-2654160-1553056?ie=UTF8&amp;node=14498703011">News, Magazines &amp; More</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/Movie-TV-Subscription-Services/b/ref=sd_allcat/145-2654160-1553056?ie=UTF8&amp;node=14498701011">Movies &amp; TV</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/Education-Learning-Subscription-Services/b/ref=sd_allcat/145-2654160-1553056?ie=UTF8&amp;node=14498695011">Education &amp; Learning</a>
     <a class="a-link-normal fsdLink fsdDeptLink" href="/Productivity-Software-Subscription-Services/b/ref=sd_allcat/145-2654160-1553056?ie=UTF8&amp;node=14498704011">Productivity &amp; Software</a>
    </div>
   </div>
  </div> 
 </body>
</html>
'''
path = '''<html>
 <head></head>
 <body>
  <a href="/Clothing/b/ref=sv_sl_fl_1040660?ie=UTF8&amp;node=1040660"><h3>CLOTHING</h3></a>
 </body>
</html>
'''
'''
测试Beautifulsoup解析有内嵌标签的文本获取

# soup = BeautifulSoup(filename, 'lxml')
soup = BeautifulSoup(path, "lxml")

category_name = soup.find('a').get_text()
category_name2 = soup.find('a').find('h3').get_text()
print(category_name)
print("-"*30)
print(category_name2)

'''

'''
测试获取Amason26个大类别的本地解析

# fsdDeptBoxes = soup.find_all(attrs={'class': re.compile('fsdDeptBox')})
# for fsdDeptBox in fsdDeptBoxes:
#     parents_title = fsdDeptBox.find(attrs={'class': "fsdDeptTitle"}).get_text()
#     all_a = fsdDeptBox.find_all(attrs={'class': 'a-link-normal fsdLink fsdDeptLink'})
#     # print(all_a)
#     a_list = []
#     for a in all_a:
#         a_dict = {}
#         a_title = a.get_text()
#         a_href = a.attrs['href']
#         if 'node=' in a_href:
#             id = eval(a_href.split("node=")[-1])
#         else:
#             id = " "
#
#         a_dict['child_id'] = id
#         a_dict['child_title'] = a_title
#         a_dict['child_href'] = "https://www.amazon.com" + a_href
#
#         a_list.append(a_dict)
#     print({parents_title: a_list})
'''

import re


def get_page_source(url, proxies=None):
    proxies = {
        'http': 'http://121.31.177.224:8123',
        'https': 'https://121.31.177.224:8123',
        # 'https': 'https://219.135.164.245:3128'
        # 'http': 'http://114.113.126.86:80'
    }
    if proxies is not None:
        r = requests.get(url, proxies=proxies, timeout=12)
    else:
        r = requests.get(url, timeout=12)
    print(r.status_code)
    return r.text


def main():
    html = '''
    <div class="wrap">
        <div id="container">
            <ul class="list">
                 <li class="item-0">first item</li>
                 <li class="item-1"><a href="https://ask.hellobi.com/link2.html">second item</a></li>
                 <li class="item-0 active"><a href="https://ask.hellobi.com/link3.html"><span class="bold">third item</span></a></li>
                 <li class="item-1 active"><a href="https://ask.hellobi.com/link4.html">fourth item</a></li>
                 <li class="item-0"><a href="https://ask.hellobi.com/link5.html">fifth item</a></li>
             </ul>
         </div>
     </div>
    '''
    doc = pq(html)
    item = doc('.wrap > #container > .list')
    print(item)
    # print(doc('li:first_child'))
    print(item.find('li:first-child'))

if __name__ == "__main__":
    main()

