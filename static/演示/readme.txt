【使用说明】

1)通常演示文件放在一个目录里，比如：demo\。与gocWeb.html在同一文件夹。

2)进入demo，点击打开“演示程序.html”即可。建议使用较新版本浏览器。


【DIY演示说明】

1)根目录名设为变量：#root，比如：#root="demo"

2)所有修改集中在 #root/js/data.js文件。

3)文件里有一个codes数组，codes[0]里是默认全局配置，其中有：
   author: 本演示的制作人
   title : 页面上方显示的标题
   path  : 演示用到的图片、声音等文件的相对路径。
           默认"#root\\media\\"可省略。
   gocURL: 对应的gocWeb.html的地址。
           默认"..\\gocWeb.html"可省略。

4)每个演示题主要有：
   title : 问题标题
   detail: 问题描述
   code  : 演示程序代码。每行需要用引号括起来。
           语句中多有双引号，建议使用单引号括起来。
   pic	 : 问题描述栏右边的图片所在目录。可缺少。
   cin   : 对cinWin窗口赋初值。
           比如： "1 2 3 4 5 6 7 8 9 10"。
   codeView: 设定本题是否可以看程序代码。

注意：code是必须的，其他可以缺省。

