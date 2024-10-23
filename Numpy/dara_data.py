import requests
from bs4 import BeautifulSoup
import pandas as pd

img_list=[]
product_buy_list=[]
detail_list=[]
price_list=[]

url='https://www.amazon.in/s?i=computers&rh=n%3A1375424031&s=popularity-rank&fs=true&ref=lp_1375424031_sar'
res=requests.get(url)
soup=BeautifulSoup(res.content,'lxml')
if res.status_code == 200:
    div=soup.find_all('div',class_='puis-card-container s-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin puis puis-v2ey9szvyi6a6t2vfpv80hgfona s-latency-cf-section puis-card-border')
    for d in div:
        product_img=d.find('div',class_='s-product-image-container aok-relative s-text-center s-image-overlay-grey puis-image-overlay-grey s-padding-left-small s-padding-right-small puis-spacing-small s-height-equalized puis puis-v2ey9szvyi6a6t2vfpv80hgfona')
        p=product_img.find('div',class_='a-section aok-relative s-image-square-aspect').img['src']
        detail=d.find('div',class_='a-section a-spacing-small puis-padding-left-small puis-padding-right-small')
        detail_list.append(detail.find('span').text.strip())
        product_buy=detail.find('div',class_='a-row a-size-base')
        product_buy_list.append(product_buy.span.text.strip())
        price_div=detail.find('div',class_='a-row a-size-base a-color-base')
        price_list.append(price_div.find('span',class_='a-offscreen').text.strip())
        img_list.append(p)
    
    df=pd.DataFrame({
        'product_img':img_list,
        'product_details':detail_list,
        'total_buy':product_buy_list,
        'price':price_list
    })
    df.to_csv('amazon_laptop_details.csv',index=False)   