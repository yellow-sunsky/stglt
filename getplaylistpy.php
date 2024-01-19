<?php
// 定义要获取的网页地址
$url = "https://strtv.dahuawang.com/b/a/2024/1/18/content_dahua_82859.shtml";
// 使用file_get_contents函数读取网页内容
$html = file_get_contents($url);
// 使用正则表达式匹配MP4视频文件的链接
preg_match('/<video src="(.+?\.mp4)"[^>]*>/i', $html, $matches);
// 如果找到了匹配的链接，就输出它
if (isset($matches[1])) {
    echo "视频文件的链接是：" . $matches[1] . "\n";
} else {
    echo "没有找到视频文件的链接。\n";
}
?>
