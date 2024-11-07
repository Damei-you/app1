from django.http import HttpResponse

def index(request):
  line1 = '<h1 style = "test-align: center">我的第一个网页</h1>'
  line2 = '<img src="https://tse4-mm.cn.bing.net/th/id/OIP-C.hHZIHh6JsWRMhslZKNlYWQHaBe?w=318&h=69&c=7&r=0&o=5&dpr=1.5&pid=1.7" width = 1300>'
  line3 = '<hr>'
  line4 = '<a href="/play/">进入游戏界面</a>'
  return HttpResponse(line1 + line4 + line3 + line2)

def play(request):
  line1 = '<h1 style = "test-align: center">游戏界面</h1>' 
  line3 = '<a href="/"> 返回主界面</a>'
  line2 = '<img src="https://cn.bing.com/images/search?view=detailV2&ccid=TwLXF0oO&id=9E4C3CD33370ACFEA739D8AC570957FE15837F4E&thid=OIP.TwLXF0oODuE9OQM2dVwxcgHaDb&mediaurl=https%3a%2f%2fforum.robloxdev.cn%2fuploads%2fdefault%2foriginal%2f2X%2f9%2f923c3cbfbc7749d9e765af476fbf7c447b011d8b.jpeg&exph=256&expw=553&q=%e6%9c%af%e5%a3%ab%e4%b9%8b%e6%88%98%e5%9b%be%e7%89%87&simid=608042584049412178&FORM=IRPRST&ck=2638C3657F38310E2F5FFD38B70CD9DC&selectedIndex=11&itb=0" width = 1300>'
  return HttpResponse(line1 + line3 + line2) 
