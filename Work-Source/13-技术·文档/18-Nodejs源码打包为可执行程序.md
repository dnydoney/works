# 技术·文档 | nodejs源码打包为可执行程序
-----------------------------------------------------------------

electron:
npm install -g electron electron-packager
git clone https://github.com/electron/electron-quick-start.git
将代码加到mainWindow之前
electron-packager .
特点：可以包含html，生成包比较大

nw.js:
https://dl.nwjs.io/v0.35.0/nwjs-v0.35.0-win-x64.zip
package.json等文件放到同目录下
执行nw
特点：可以包含html，生成包比较大

app.js
http://dl.bintray.com/sihorton/appjs/appjs-0.0.20-win32-ia32.zip
特点：可以包含html，体积适中

jxcore:
https://raw.githubusercontent.com/jxcore/jxcore-release/master/0311/jx_win64v8.zip
jx package index.js index
jx index.js
特点：只能包含js，体积小

nexe:
npm install -g nexe
nexe index.js -o test.exe
特点：只能包含js，体积小

pkg:
npm install -g pkg
pkg -t win index.js -o test.exe
特点：只能包含js，体积小
