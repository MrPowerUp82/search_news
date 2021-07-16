#coding: utf-8
import requests
from lxml import html

url='https://noticias.uol.com.br/ultimas/'
headers={
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36",
    "Accept" : "*/*"
}
page=requests.get(url,headers=headers)
tree=html.fromstring(page.content)
list_links=tree.xpath('//div[@class="thumbnails-wrapper"]/a/@href')
for link in list_links:
    name_file=link.split('/')
    for n in name_file:
        if '.htm' or '.shtm' in n:
            index=name_file.index(n)

    name_file=name_file[index]
    name_file=name_file.split('.')
    name_file=name_file[0]
    name_file=name_file+'.html'
    page=requests.get(link,headers=headers)
    tree=html.fromstring(page.content)
    text=tree.xpath('//div[@class="text  "]/*[self::p or self::h2]/text()')
    arq=open(name_file,'w')
    arq.write('<center>\n')
    arq.close()
    for p in text:
        arq=open(name_file,'a')
        arq.write('<p>{}</p><br>\n'.format(p))
        arq.close()

    arq=open(name_file,'a')
    arq.write('<center>')
    arq.close()


