# GoCli 使用说明



使用set进行环境变量设置时，只对当前对话框程序有效。当cmd设置对话框关闭时，环境变量复原。如：

set PATH=%PATH%;C:\Program Files\ 
永久修改系统环境变量。使用setx 。如：

setx PATH "%PATH%;C:\Program Files\"  /M


set PATH=%PATH%;C:\Users\doney.000\AppData\Roaming\Pub\Cache\bin





```
flutter pub global activate --source  path  G:\flutter-source\flutter-go\go-cli
```

