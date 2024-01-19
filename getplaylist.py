# 导入requests和BeautifulSoup库
import requests
from bs4 import BeautifulSoup
# 定义要获取的网页地址
url = "https://strtv.dahuawang.com/b/a/2024/1/18/content_dahua_82859.shtml"
# 使用requests.get函数发送请求
r = requests.get(url)
# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(r.content, "html.parser")
# 使用find_all函数查找所有的video标签
videos = soup.find_all("video")
# 如果找到了video标签，就从中提取src属性的值，即视频文件的链接
if videos:
    video_link = videos[0]["src"]
    print("视频文件的链接是：" + video_link)
else:
    print("没有找到视频文件的链接。")
