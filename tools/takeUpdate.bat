@ECHO OFF
echo 提交当前任务至服务器
cd /d f:\works
echo 当前工作路径为：%cd%
git add .
git commit -m "push work logs"
echo 提交文件
git push
PAUSE