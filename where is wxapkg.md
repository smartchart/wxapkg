# wxapkg 目录
## 安卓手机
* 前提:安卓手机需获取root权限
*     1.下载RE文件管理器并给与root权限
    
*     2.打开文件路径：/data/data/com.tencent.mm/MicroMsg/{User}/appbrand/pkg     其中User为一串md5字符串如右图所示    


![Image](https://raw.githubusercontent.com/smartchart/wxapkg/master/image/user.jpg)

*	  3.打开第一个文件夹，再打开appbrand/pkg文件夹 可以看到该文件夹下文件均为.wxapkg文件，清空该文件下所有文件，微信端再次进入小程序会产生新的.wxapkg文件，如图所示。


![Image](https://raw.githubusercontent.com/smartchart/wxapkg/master/image/wxapkg.jpg)  