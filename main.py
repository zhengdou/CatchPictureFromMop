#coding=utf-8
import urllib
import urllib2
import re
import time

def getHtml(url):
    user_agent='Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
    headers={'User-Agent':user_agent}
    request=urllib2.Request(url,headers=headers)
    page=urllib2.urlopen(request)
    return page.read()

def getJPEGImg(html):
    reg=r'src="(.+?\.JPEG)"'
    getImg(html,reg)

def getjpgImg(html):
    reg=r'src="(.+?\.jpg790x600.jpg)"'
    getImg(html,reg)


def getImg(html,reg):
    x=0
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    for imgurl in imglist:
        name=str(time.time())
        fileName=name[0:10]+str(x)
        urllib.urlretrieve(imgurl,'%s.jpg' % fileName)
        x=x+1

        
#去除列表重复元素        
def dealList(List):
    newList=[]
    for i in List:
        if i not in newList:
            newList.append(i)
    return newList

    
def getAllUrl(html):
    reg=r'<a target="_blank" href="(/.+?\.html)"'
    newUrl=re.compile(reg)
    allUrl=re.findall(newUrl,html)
    return allUrl
        
            
for tail in range(90):
    urlList=[]
    strTail=str(tail+8)
    print"********************"
    print strTail
    print'**********************'
    strUrl='http://tt.mop.com/c35/0/1_'+strTail+'.html'
    html=getHtml(strUrl)
    urlList=getAllUrl(html)
    urlList=dealList(urlList)
    for i in urlList:
        url="http://tt.mop.com"+i
        print url
        print
        html=getHtml(url)
        getJPEGImg(html)
        getjpgImg(html)

