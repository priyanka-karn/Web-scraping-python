from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("C://users/pkarna/chromedriver_win32")


#Scraping the data from website
driver.get("<a href="/restaurants/bhagat-halwai-dayal-bagh-shahganj-dayal-bagh-agra-74562" class="_1j_Yo"><div class="_1HEuF"><div class="_3FR5S"><div class="efp8s"><img class="_2tuBw _12_oN" alt="Bhagat Halwai (Dayal Bagh)" width="254" height="160" src="https://res.cloudinary.com/swiggy/image/upload/fl_lossy,f_auto,q_auto,w_508,h_320,c_fill/crfkxcc5jbvdgmxioey2"></div><div class="IJsqo" style="background: rgb(58, 60, 65); color: rgb(255, 255, 255); border-color: rgb(30, 32, 35) transparent;"><div class="_1kXWW">Promoted</div></div><div class="_3Ztcd"><div class="nA6kb">Bhagat Halwai (Dayal Bagh)</div><div class="_1gURR" title="Chinese, North Indian, Sweets, South Indian, Chaat">Chinese, North Indian, Sweets, South Indian, Chaat</div></div><div class="_3Mn31"><div class="_9uwBC _2lAlc"><span class="icon-star _537e4"></span><span>3.9</span></div><div>•</div><div>33 MINS</div><div>•</div><div class="nVWSi">₹250 FOR TWO</div></div><div class="Zlfdx"><span class="icon-offer-filled _2fujs"></span><span class="sNAfh">40% off | Use TRYNEW</span></div></div><div class="_3B2qG"><span role="button" aria-label="Open" class="_2ECk4 _24tlh">Quick View</span></div></div></a>")


content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_1j_Yo'}):
name=a.find('div', attrs={'class':'_1HEuF'})
price=a.find('div', attrs={'class':'_3FR5S'})
rating=a.find('div', attrs={'class':'efp8s'})
products.append(name.text)
prices.append(price.text)
ratings.append(rating.text)


#Finding the minimum price

min_price = min(prices)
print('Minimum price' , min_price)
