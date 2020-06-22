

###  2020年03月11日
-----------------------------------------------------------------
Flutter 第一次运行就出现白屏的问题
解决办法：

顶部菜单找到 run-->Edit Configurations 中加这么一句：
--enable-software-rendering



###  2020年03月05日

-----------------------------------------------------------------

## 常用命令

1.编译：
* `flutter packages get`: 获取flutter packages包

2.运行：
* `flutter run` （默认为debug环境）
* `flutter run --release` (以release模式运行)

3.安装
* 帮助：`flutter -h` 或 `flutter --help`
* 诊断flutter：`flutter doctor`
* 查看flutter版本号：`flutter --version`
* flutter升级：`flutter upgrade`

4.打包apk包：
* 直接打包：
`flutter build apk`
* 64位-release：
`flutter build apk --release --target-platform android-arm64`
* 32位-release：
`flutter build apk --release --target-platform android-arm`











###  2020年03月25日

-----------------------------------------------------------------

### 1.主题色主题色设置



```swift
class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter Demo',//针对Android 里面可用
      theme: ThemeData(
        primarySwatch: Colors.yellow,//主题色设置，深色：则时间和电池颜色为白色；浅色：则时间和电池颜色为黑色
        highlightColor: Color.fromRGBO(1, 0, 0, 0.0),//去掉tabBar默认选中效果
        splashColor: Color.fromRGBO(1, 0, 0, 0.0),//去掉tabBar默认选中效果
      ),
      home: RootPage(),
    );
  }
}
```



### 

**`MediaQuery.removePadding` -> `removeTop: true`**



```swift
Container(
  color: Color.fromRGBO(220, 220, 220, 1.0),
  child: MediaQuery.removePadding(
    removeTop: true,
    context: context,
    child: ListView(
      children: <Widget>[
        Container(
          color: Colors.white,
          height: 200,
        ),
        SizedBox(height: 10,),
        DiscoverCell(imageName: 'images/微信支付1.png',title: '支付',),
      ],
    ),
  ),
),
```

### 3.Image设置圆角



```swift
Row(
children: <Widget>[
  Container(
    width: 70,
    height: 70,
   // child: Image(image: AssetImage('images/Steven.png'),),//写在此处设置圆角无效
    decoration: BoxDecoration(
      color: Colors.blue,
      borderRadius: BorderRadius.circular(10.0),
      image: DecorationImage(image:AssetImage('images/Steven.png'),
      fit: BoxFit.cover)//设置图片的填充模式
    ),
  ),//头像
  Container(),//右边部分
],
)
```

### 4.设备的宽高获取



```swift
width: MediaQuery.of(context).size.width,
height: MediaQuery.of(context).size.height,
```

### 5.文字居中方向设置



```swift
//Container属性
alignment: Alignment.centerLeft,
```

### 6.网络图片和本地图片的加载



```swift
Container(
  width: 34,
  height: 34,
  margin: EdgeInsets.all(10),
  decoration: BoxDecoration(
      borderRadius: BorderRadius.circular(6.0),
      image: DecorationImage(
        image: imageUrl != null
            ? NetworkImage(imageUrl) //网络图片
            : AssetImage(imageAssets),//本地图片
      )),
)
```

### 7.链式编程-添加数据



```swift
 @override
 //数据、对象创建
  void initState() {
    super.initState();
    //链式编程，调用两次addAllData并返回数组到 _listDatas
    _listDatas..addAll(datas)..addAll(datas);
    //数据排序
    _listDatas.sort((Friends a, Friends b){
      return a.indexLetter.compareTo(b.indexLetter);
    });
    //print('_listDatas:$_listDatas');
  }
```

### 8.相除取整

```
~/
```



```swift
onVerticalDragUpdate: (DragUpdateDetails details){
  print(details.globalPosition.dy);//相对于整个屏幕的值
  RenderBox box = context.findRenderObject();
  //计算当前位置 坐标转换, 算出y值
  double y = box.globalToLocal(details.globalPosition).dy;
  //y值除以每个item的高度就是当前的索引
  //每一个item的高度
  var itemH = ScreenHeight(context)/2/INDEX_WORDS.length;
  int index = y ~/ itemH;//相除取整
  print(box.globalToLocal(details.globalPosition));
},
```

### 9.数组越界处理



```swift
//使用clamp
//取值范围0~INDEX_WORDS.length-1 添加安全判断 
int index = (y ~/ itemHeight).clamp(0, INDEX_WORDS.length - 1);
```

### 10.定义回调函数和调用



```swift
//定义回调函数
final void Function(String str) indexBarCallBack;
//构造方法
const IndexBar({Key key, this.indexBarCallBack}) : super(key: key);
//调用该callBack
//监听所在位置：计算当前位置
onVerticalDragUpdate: (DragUpdateDetails details){
  widget.indexBarCallBack(getIndex(context, details.globalPosition));
},
//外部使用
IndexBar(
    indexBarCallBack: (String str){
      print("收到了：$str");
    },
  ),
```

### 11.PopupMenuButton 使用



```swift
Container(
    margin: EdgeInsets.only(right: 10),
    child: PopupMenuButton(
      offset: Offset(0, 60.0),
      child: Image(image: AssetImage('images/圆加.png'),width: 25,),
      itemBuilder: _buildPopupMenuItem,
    ),
  )
    //创建Item的方法！
  PopupMenuItem<String> _buildItem(String imgAss, String title) {
    return PopupMenuItem(
      child: Row(
        children: <Widget>[
          Image(
            image: AssetImage(imgAss),
            width: 20,
          ),
          Container(
            width: 20,
          ),
          Text(
            title,
            style: TextStyle(color: Colors.white),
          ),
        ],
      ),
    );
  }

//回调方法
  List<PopupMenuItem<String>> _buildPopupMenuItem(BuildContext context) {
    return <PopupMenuItem<String>>[
      _buildItem('images/发起群聊.png', '发起群聊'),
      _buildItem('images/添加朋友.png', '添加朋友'),
      _buildItem('images/扫一扫1.png', '扫一扫'),
      _buildItem('images/收付款.png', '收付款'),
    ];
  }
```

### 设置popup背景颜色



```swift
//MaterialApp -> theme -> cardColor
MaterialApp(
  debugShowCheckedModeBanner: false,
  title: 'Flutter Demo',//针对Android 里面可用
  theme: ThemeData(
    primarySwatch: Colors.yellow,//主题色设置，深色：则时间和电池颜色为白色；浅色：则时间和电池颜色为黑色
    highlightColor: Color.fromRGBO(1, 0, 0, 0.0),//去掉tabBar默认选中效果
    splashColor: Color.fromRGBO(1, 0, 0, 0.0),//去掉tabBar默认选中效果
    cardColor: Color.fromRGBO(1, 1, 1, 0.65),//设置popup背景颜色
  ),
  home: RootPage(),
)
```

### 效果图：

![img](https:////upload-images.jianshu.io/upload_images/4637097-04f5852117ca787b.gif?imageMogr2/auto-orient/strip|imageView2/2/w/410/format/webp)

PopupMenuButton

### 12.滑动ListView让键盘消失

```
FocusScope.of(context).requestFocus(FocusNode());
```



```swift
//监听ListView的滑动事件，让键盘消失
Expanded(
    flex: 1, //占据剩余空间
    child: MediaQuery.removePadding(
      context: context,
      removeTop: true,
      child: NotificationListener(
        onNotification: (ScrollNotification note){
          FocusScope.of(context).requestFocus(FocusNode());
        },//滑动让键盘消失
        child: ListView.builder(
          itemCount: _models.length,
          itemBuilder: _itemForRow,
        ),
      ),
    ),
  )
```

### 13.Containter 设置部分圆角和阴影效果



```swift
 @override
  Widget build(BuildContext context) {
    return Container(
      padding: EdgeInsets.only(top: 10, bottom: 10),
      decoration: BoxDecoration(
        color: Colors.white,
        // 设置阴影 要在裁剪之外添加一个Containter里面处理，否则无效
        boxShadow: [
          BoxShadow(
              color: Color(0xff333333).withOpacity(0.05),
              offset: Offset(0, 1.0),
              blurRadius: 5),
        ],
      ),
      child: new ClipRRect(
        // 设置局部圆角
        borderRadius: BorderRadius.only(
          bottomLeft: Radius.circular(5),
          bottomRight: Radius.circular(5),
        ),
        child: Container(
          height: ScreenUtil().setHeight(147),
          child: Container(
            margin: EdgeInsets.only(left: 40, right: 40),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: navigatorList.map((item) {
                return _navigatorItem(context, item);
              }).toList(),
            ),
          ),
        ),
      ),
    );
  }
```

### 14. Scaffold 的 appBar 去掉底部阴影



```swift
return Scaffold(
  appBar: AppBar(
    backgroundColor: Colors.white,
    centerTitle: true,
    title: Text(
      "发现",
      style: TextStyle(
          color: Color(0xff333333), fontSize: ScreenUtil().setSp(34)),
    ),
    bottomOpacity: 0,
    elevation: 0, // 去掉底部阴影
  ),
);
```

### 15.Image图片设置宽度自适应



```swift
Container(
    margin: EdgeInsets.only(left: 15, right: 15),
    height: ScreenUtil().setHeight(243),
    decoration: BoxDecoration(
        image: DecorationImage(
      image: NetworkImage(
          'http://fdfs.xmcdn.com/group63/M0A/99/95/wKgMaFz_RD-BDyFjAAIO0iRtj0U176.jpg'),
      fit: BoxFit.fitWidth,
      alignment: Alignment.topCenter,
    )),
  ),
```

### 16.FlutterListView嵌套GridView滚动冲突问题

> ListView和GirdView都是滚动Widget 两个部件嵌套就会存在滚动冲突，解决办法如下



```swift
body: new ListView(
          shrinkWrap: true,
          padding: EdgeInsets.all(0),
          children: <Widget>[
            new GridView.count(
             padding: EdgeInsets.all(0),
            physics: new NeverScrollableScrollPhysics(),//增加
            shrinkWrap: true,//增加
            crossAxisCount: 3,
            children:<Widget>[]
          ],
        ),
```

##### ① 处理listview嵌套报错



```swift
shrinkWrap: true,
```

##### ②处理GridView中滑动父级Listview无法滑动



```swift
physics: new NeverScrollableScrollPhysics();
```

### 17.Flutter 自定义TabBar和修改indiactor 宽度

#### 1. 关键代码



```swift
import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';

class FriendsList extends StatefulWidget {
  @override
  _FriendsListState createState() => _FriendsListState();
}
class _FriendsListState extends State<FriendsList>
    with SingleTickerProviderStateMixin {
  TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(initialIndex: 0, length: 2, vsync: this);
  }

  @override
  void dispose() {
    super.dispose();
    _tabController.dispose();
  }
  
  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 2,
      child: Scaffold(
        appBar: AppBar(
          title: Container(
              height: ScreenUtil().setHeight(73),
              alignment: Alignment.topLeft,
              child: TabBar(
                tabs: [
                  Tab(text: '好友'),
                  Tab(text: '心动'),
                ],
                controller: _tabController,
                indicatorWeight: 2,
                indicatorPadding: EdgeInsets.only(left: 10, right: 10),
                labelPadding: EdgeInsets.symmetric(horizontal: 10),
                isScrollable: true,
                indicatorColor: Color(0xffFF7E98),
                labelColor: Color(0xffFF7E98),
                labelStyle: TextStyle(
                  fontSize: ScreenUtil().setSp(36),
                  color: Color(0xffFF7E98),
                  fontWeight: FontWeight.w500,
                ),
                unselectedLabelColor: Color(0xffAAAAAA),
                unselectedLabelStyle: TextStyle(
                    fontSize: ScreenUtil().setSp(32), color: Color(0xffAAAAAA)),
                indicatorSize: TabBarIndicatorSize.label,
              )),
          backgroundColor: Colors.white,
          elevation: 0,
        ),
        body: TabBarView(
          children: [
            Container(
              child: Center(
                child: Text("好友页面"),
              ),
            ),
            Container(
              child: Center(
                child: Text("心动页面"),
              ),
            ),
          ],
          controller: _tabController,
        ),
      ),
    );
  }
}
```

#### 2. 效果图

![img](https:////upload-images.jianshu.io/upload_images/4637097-a32f0eda94fa7280.gif?imageMogr2/auto-orient/strip|imageView2/2/w/340/format/webp)

效果图.gif

### 18 fluro 插件 实现appBar不要出现返回键

Application.router.navigateTo(context, "/index",replace: true);

### 19.文字溢出处理

#### ①Expanded + TextOverflow.ellipsis 设置省略号



```swift
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("LayoutPage")),
      body: Center(
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Icon(
              Icons.star,
              size: 16.0,
              color: Colors.grey,
            ),
            Padding(padding: new EdgeInsets.only(left: 5.0)),
            Expanded(
              child: Text(
                "100010001000100010001000100010001000100010001000100010001000100010001000100010001000100010001000",
                style: new TextStyle(color: Colors.grey, fontSize: 14.0),
                // 设置省略号
                overflow: TextOverflow.ellipsis,
                // 设置最大行数
                maxLines: 1,
              ),
            )
          ],
        ),
      ),
    );
  }
```

#### ② Expanded + TextOverflow.ellipsis 不生效

> 通过

- 限定Container 宽度
- Row 布局嵌套 Expanded 可以添加约束

![img](https:////upload-images.jianshu.io/upload_images/4637097-51116930ba6d0b54.png?imageMogr2/auto-orient/strip|imageView2/2/w/625/format/webp)

TextOverflow.ellipsis 不生效

### 20.数据解析报错之关键字 do

do 为关键字，不能设置为Model的属性，应该用其他名称替换



```swift
class UserChatList {
  int doType;
  UserChatList({this.doType});
  UserChatList.fromJson(Map<String, dynamic> json) {
    doType = json['do'];
  }
```

### 21.聊天消息UI搭建

#### 效果图

![img](https:////upload-images.jianshu.io/upload_images/4637097-10b865363df83b38.png?imageMogr2/auto-orient/strip|imageView2/2/w/369/format/webp)

聊天消息U

> 思路

- ①Positison 设置



```swift
right: ScreenUtil().setWidth(20),
bottom: -ScreenUtil().setHeight(50),
```

- ② Stack 设置溢出显示



```swift
overflow: Overflow.visible
```

#### 关键代码



```swift
/// 聊天Widget
  Widget ChatWidget(String chatType, String msg) {
    // 1 发出者
    if (chatType == 'send') {
      return Container(
        decoration: BoxDecoration(
          color: Colors.white,
          // 设置阴影
          boxShadow: [
            BoxShadow(
              color: Color(0xffFF7E98),
              offset: Offset(0, 1),
              blurRadius: 8,
            )
          ],
          borderRadius: BorderRadius.only(
              topLeft: Radius.circular(15),
              topRight: Radius.circular(15),
              bottomRight: Radius.circular(15)),
        ),
        height: ScreenUtil().setHeight(80),
        margin: EdgeInsets.only(
          top: ScreenUtil().setHeight(40),
        ),
        padding: EdgeInsets.only(
            left: ScreenUtil().setWidth(40),
            right: ScreenUtil().setWidth(40),
            top: ScreenUtil().setHeight(10),
            bottom: ScreenUtil().setHeight(10)),
        child: Text(
          msg != null && msg.length > 0 ? msg : '',
          style: TextStyle(
              fontSize: ScreenUtil().setSp(30), color: Color(0xff333333)),
          maxLines: 1,
          overflow: TextOverflow.ellipsis,
        ),
      );
    } else if (chatType == 'minisend') {
      return Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: <Widget>[
          Stack(
            overflow: Overflow.visible,
            children: <Widget>[
              // 消息
              Container(
                decoration: BoxDecoration(
                  color: Colors.white,
                  // 设置阴影
                  boxShadow: [
                    BoxShadow(
                      color: Color(0xffFF7E98),
                      offset: Offset(1, 1),
                      blurRadius: 8,
                    )
                  ],
                  borderRadius: BorderRadius.only(
                      topLeft: Radius.circular(15),
                      topRight: Radius.circular(15),
                      bottomRight: Radius.circular(15)),
                ),
                height: ScreenUtil().setHeight(80),
                margin: EdgeInsets.only(
                  top: ScreenUtil().setHeight(40),
                ),
                padding: EdgeInsets.only(
                    left: ScreenUtil().setWidth(40),
                    right: ScreenUtil().setWidth(40),
                    top: ScreenUtil().setHeight(10),
                    bottom: ScreenUtil().setHeight(10)),
                child: Text(
                  '😊很想认识你😊',
                  style: TextStyle(
                      fontSize: ScreenUtil().setSp(30),
                      color: Color(0xff333333)),
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                ),
              ),
              Positioned(
                right: ScreenUtil().setWidth(20),
                bottom: -ScreenUtil().setHeight(50),
                child: // 小程序路径
                    Container(
                  margin: EdgeInsets.only(top: ScreenUtil().setHeight(16)),
                  child: Row(
                    children: <Widget>[
                      Text(
                        '去小程序查看',
                        style: TextStyle(
                            fontSize: ScreenUtil().setSp(22),
                            color: Color(0xffFF7E98)),
                      ),
                      Icon(
                        MyIcons.sex_boy,
                        size: ScreenUtil().setSp(16),
                        color: Color(0xffFF7E98),
                      )
                    ],
                  ),
                ),
              ),
            ],
          ),
        ],
      );
    } else if (chatType == 'mine') {
      return Row(
        mainAxisAlignment: MainAxisAlignment.end,
        children: <Widget>[
          Container(
            decoration: BoxDecoration(
              color: Colors.white,
              // 设置阴影
              boxShadow: [
                BoxShadow(
                  color: Color(0xffFF7E98),
                  offset: Offset(0, 1),
                  blurRadius: 8,
                )
              ],
              // 设置渐变色
              gradient: LinearGradient(
                colors: [Color(0xFFFF7E98), Color(0xFFFD7BAB)],
                begin: Alignment(-1, -1),
                end: Alignment(1.0, 0.56),
              ),
              // 设置圆角
              borderRadius: BorderRadius.only(
                  topLeft: Radius.circular(15),
                  topRight: Radius.circular(15),
                  bottomLeft: Radius.circular(15)),
            ),
            height: ScreenUtil().setHeight(80),
            margin: EdgeInsets.only(
              top: ScreenUtil().setHeight(40),
            ),
            padding: EdgeInsets.only(
                left: ScreenUtil().setWidth(40),
                right: ScreenUtil().setWidth(40),
                top: ScreenUtil().setHeight(10),
                bottom: ScreenUtil().setHeight(10)),
            child: Text(
              msg != null && msg.length > 0 ? msg : '',
              style: TextStyle(
                  fontSize: ScreenUtil().setSp(30), color: Colors.white),
              maxLines: 1,
              overflow: TextOverflow.ellipsis,
            ),
          )
        ],
      );
    } else {
      return Container(
        margin: EdgeInsets.only(bottom:ScreenUtil().setHeight(40) ),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.end,
          children: <Widget>[
            Stack(
              overflow: Overflow.visible,
              children: <Widget>[
                Container(
                  decoration: BoxDecoration(
                    color: Colors.white,
                    // 设置阴影
                    boxShadow: [
                      BoxShadow(
                        color: Color(0xffFF7E98),
                        offset: Offset(0, 1),
                        blurRadius: 8,
                      )
                    ],
                    // 设置渐变色
                    gradient: LinearGradient(
                      colors: [Color(0xFFFF7E98), Color(0xFFFD7BAB)],
                      begin: Alignment(-1, -1),
                      end: Alignment(1.0, 0.56),
                    ),
                    // 设置圆角
                    borderRadius: BorderRadius.only(
                        topLeft: Radius.circular(15),
                        topRight: Radius.circular(15),
                        bottomLeft: Radius.circular(15)),
                  ),
                  height: ScreenUtil().setHeight(80),
                  margin: EdgeInsets.only(
                    top: ScreenUtil().setHeight(40),
                  ),
                  padding: EdgeInsets.only(
                      left: ScreenUtil().setWidth(40),
                      right: ScreenUtil().setWidth(40),
                      top: ScreenUtil().setHeight(10),
                      bottom: ScreenUtil().setHeight(10)),
                  child: Text(
                    msg != null && msg.length > 0 ? msg : '',
                    style: TextStyle(
                        fontSize: ScreenUtil().setSp(30), color: Colors.white),
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                  ),
                ),
                // 小程序路径
                Positioned(
                  left: ScreenUtil().setWidth(20),
                  bottom: -ScreenUtil().setHeight(50),
                  child: Container(
                    margin: EdgeInsets.only(top: ScreenUtil().setHeight(16),),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.end,
                      children: <Widget>[
                        Text(
                          '去小程序查看',
                          style: TextStyle(
                              fontSize: ScreenUtil().setSp(22),
                              color: Color(0xffFF7E98)),
                        ),
                        Icon(
                          MyIcons.sex_boy,
                          size: ScreenUtil().setSp(16),
                          color: Color(0xffFF7E98),
                        )
                      ],
                    ),
                  ),
                ),
              ],
            )
          ],
        ),
      );
    }
  }
```

### 22. Flutter 复制到剪切板

> 通过Clipboard实现复制操作

#### 1.声明key并在Scaffold指定key



```swift
/// 剪切板Key
final clicpBoardKey  = new GlobalKey<ScaffoldState>();
return Scaffold(
key: clicpBoardKey,
);
```

#### 2.实现复制操作并弹出SnackBar



```swift
Clipboard.setData(ClipboardData(text: '人生若只初相见'));
clicpBoardKey.currentState.showSnackBar(SnackBar(content: Text('已复制到剪贴板')));
```

### 23.Url 转义 decode



```swift
decodeURIComponent('%2Fpage%2Forigin%2Forigin%3Fuid%3D')
```

### 24.获取widget 控件的尺寸



```swift
// 宽度
width: MediaQuery.of(context).size.width,
// 高度
height: MediaQuery.of(context).size.height * 0.05,
// 注意: context 为父组件的context
```

### 25.decoration相关

#### 1) 边框



```swift
// 同时设置4条边框：1px粗细的黑色实线边框
BoxDecoration(
  border: Border.all(color: Colors.black, width: 1, style: BorderStyle.solid)
)

// 设置单边框：上边框为1px粗细的黑色实线边框，右边框为1px粗细的红色实线边框
BoxDecoration(
  border: Border(
    top: BorderSide(color: Colors.black, width: 1, style: BorderStyle.solid),
    right: BorderSide(color: Colors.red, width: 1, style: BorderStyle.solid),
  ),
)
```

#### 2) 圆角



```swift
// 同时设置4个角的圆角为5
BoxDecoration(
  borderRadius: BorderRadius.circular(5),
)

// 设置单圆角：左上角的圆角为5，右上角的圆角为10
BoxDecoration(
  borderRadius: BorderRadius.only(
    topLeft: Radius.circular(5),
    topRight: Radius.circular(10),
  ),
)
```

#### 3) 阴影



```swift
BoxDecoration(
  boxShadow: [
    BoxShadow(
      offset: Offset(0, 0),
      blurRadius: 6,
      spreadRadius: 10,
      color: Color.fromARGB(20, 0, 0, 0),
    ),
  ],
)
```

#### 4) 渐变色



```swift
// 从左到右，红色到蓝色的线性渐变
BoxDecoration(
  gradient: LinearGradient(
    begin: Alignment.centerLeft,
    end: Alignment.centerRight,
    colors: [Colors.red, Colors.blue],
  ),
)

// 从中心向四周扩散，红色到蓝色的径向渐变
BoxDecoration(
  gradient: RadialGradient(
    center: Alignment.center,
    colors: [Colors.red, Colors.blue],
  ),
)
// 设置角度
final gradient = Utils.parseAngleToAlignment(90);
BoxDecoration(
    gradient: LinearGradient(
        colors: [
            Color(0xFFFFA3AD),
            Color(0xFFFC5E72)
        ],
        begin: Alignment(gradient['beginX'], gradient['beginY']),
        end: Alignment(gradient['endX'], gradient['endY'])
    ),
    borderRadius: BorderRadius.circular(2)
)
```

### 26.MaterialApp 使用讲解



```swift
字段  类型

home（主页）    Widget
routes（路由）  Map<String, WidgetBuilder>
theme（主题）   ThemeData
debugShowMaterialGrid（调试显示材质网格） bool

navigatorKey（导航键）   GlobalKey<NavigatorState>
onGenerateRoute（生成路由）   RouteFactory
onUnknownRoute（未知路由）    RouteFactory
navigatorObservers（导航观察器）   List<NavigatorObserver>
initialRoute（初始路由）  String
builder（建造者）    TransitionBuilder
title（标题）   String
onGenerateTitle（生成标题）   GenerateAppTitle
color（颜色）   Color
locale(地点)  Locale
localizationsDelegates（本地化委托）   Iterable<LocalizationsDelegate<dynamic>>
localeResolutionCallback（区域分辨回调）    LocaleResolutionCallback
supportedLocales（支持区域）  Iterable<Locale>
showPerformanceOverlay（显示性能叠加）  bool
checkerboardRasterCacheImages（棋盘格光栅缓存图像）    bool
checkerboardOffscreenLayers（棋盘格层）   bool
showSemanticsDebugger（显示语义调试器）  bool
debugShowCheckedModeBanner（调试显示检查模式横幅）  bool
```

### 27.使用`FutureBuilder`每调用一次setState就会重新请求`future`

解决方法：将 `future`提取出来，作为一个变量



```swift
Future<int> future;

  @override
  void initState() {
    super.initState();
    future=getInt();
  }

  FutureBuilder<int>(
    future: future,
    builder: (context, snapshot) {
      return ...;
    }
  ),

  Future<int> getInt(){
    return Future.value(1);
  }
```

### 28.输入框内容为空时，长按不显示粘贴工具栏

将输入框中的autoFocus属性为ture去掉

### 29.Flutter 左上角返回按钮回调(CallBack)

#### 1.1 async await 实现



```swift
/// 跳转到下级页面时 await Navigator.pushNamed
onTap: () async {
    await Navigator.pushNamed(context, '/account');
    //执行 刷新数据操作
    refrshData();
  },
```

#### 2.嵌套封装 会导致await 失效



```dart
class NavigatorUtil{
  /// 通用跳转
  static push(BuildContext context,Widget widget ) {
    Navigator.push(context, PageRouteBuilder(transitionDuration: Duration(milliseconds: 300),
        pageBuilder: (context, animation, secondaryAnimation){
          return new FadeTransition( //使用渐隐渐入过渡,
            opacity: animation,
            child:widget,
          );
        })
    );
  }
}

//使用导致await失效
onTap: () async {
    // 其他
     await NavigatorUtil.push(context, widget);
     //执行刷新操作
  },
```

`解决方案`
 封装层嵌套 async await



```dart
class NavigatorUtil{
  /// 通用跳转
  static push(BuildContext context,Widget widget ) async {
    await Navigator.push(context, PageRouteBuilder(transitionDuration: Duration(milliseconds: 300),
        pageBuilder: (context, animation, secondaryAnimation){
          return new FadeTransition( //使用渐隐渐入过渡,
            opacity: animation,
            child:widget,
          );
        })
    );
  }
}
```

### 30.GestureDetector 手势冲突

> 解决手势冲突 - IgnorePointer



```swift
IgnorePointer(
  child: GestureDetector(
    child: Container(
      height: ScreenUtil().setHeight(300),
      width: Screen.width,
      decoration: BoxDecoration(
        borderRadius: BorderRadius.only(
          topLeft: Radius.circular(ScreenUtil().setWidth(20)),
          topRight: Radius.circular(ScreenUtil().setWidth(20)),
        ),
        gradient: LinearGradient(
          colors: [
            Color(0xFFFFFFFF),
            Colors.white.withOpacity(.2),
            Colors.white.withOpacity(0),
            Colors.white.withOpacity(0),
            Colors.white.withOpacity(0)
          ],
          begin: Alignment(
              topGradient['beginX'], topGradient['beginY']),
          end: Alignment(topGradient['endX'], topGradient['endY']),
        ),
      ),
    ),
    onTap: () {
      backToTop();
    },
  ),
),
```

### 31.TextField  设置border 颜色(黑线修改颜色)



```swift
/// 输入框
Container(
    child: Theme(
        data: ThemeData(
                primaryColor: Colors.white, hintColor: Colors.white),
        child: TextField(
            style: TextStyle(
                fontSize: ScreenUtil().setSp(36),
                color: Colors.white,
            ),
            controller: inputController,
            onChanged: handlePhoneInput,
            autofocus: true,
            decoration: new InputDecoration(
                border: const UnderlineInputBorder(
                    borderSide: BorderSide(style: BorderStyle.solid,color: Colors.white,),
                ),
                contentPadding: EdgeInsets.only(
                    left: ScreenUtil().setWidth(100),
                    right: ScreenUtil().setWidth(20),
                    top: ScreenUtil().setWidth(20),
                    bottom: ScreenUtil().setWidth(20),
                ),
                hintText: '输入手机号',
                hintStyle: TextStyle(
                    color: Color.fromRGBO(255, 255, 255, .7),
                    fontSize: ScreenUtil().setSp(36),
                ),
            ),
        ),
    ),
),
```

### 32.decoration 阴影设置无边界

> 通过Opacity 以及 LinearGradient设置 stops节点和colors 结合



```swift
// 顶部阴影
Opacity(
  opacity: 0.23,
  child: Container(
    height: ScreenUtil().setHeight(129),
    decoration: BoxDecoration(
      gradient: LinearGradient(
          stops: [
            0,
            .8
          ],
          colors: [
            Color(0xff565656),
            Color(0xFF030303).withOpacity(0),
          ],
          begin:
              Alignment(gradient['beginX'], gradient['beginY']),
          end: Alignment(gradient['endX'], gradient['endY'])),
      borderRadius: BorderRadius.only(
        topLeft: Radius.circular(10.0),
        topRight: Radius.circular(10.0),
      ),
    ),
    child: Container(
      margin: EdgeInsets.only(
        left: ScreenUtil().setWidth(10),
        right: ScreenUtil().setWidth(17),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: <Widget>[
          Container(
            margin: EdgeInsets.only(
                top: ScreenUtil().setHeight(17)),
            child: Row(
              children: <Widget>[
                Icon(
                  MyIcons.heart,
                  size: ScreenUtil().setSp(40),
                  color: Colors.white,
                ),
                Container(
                  margin: EdgeInsets.only(
                    left: ScreenUtil().setWidth(5),
                    top: ScreenUtil().setWidth(5),
                  ),
                  child: Text(
                    this.widget.item != null &&
                            this.widget.item.praises != null
                        ? this.widget.item.praises.toString()
                        : '',
                    style: TextStyle(
                      fontSize: ScreenUtil().setSp(20),
                      color: Colors.white,
                    ),
                    textAlign: TextAlign.center,
                  ),
                )
              ],
            ),
          ),
        ],
      ),
    ),
  ),
)
```

### 33.Dart List.asMap() 获取下标



```dart
 this.list.asMap().keys.map((i) {
   // i 为下标
    return _itemUI(context, i);
  }).toList()
```

### 34.indexWhere 获取数组索引



```dart
int currentIndex = this.renderList.indexWhere((item) => item.id == feed.id);
```

### 35.build runner 插件使用

build runner 插件`编译生成属性快捷键`



```dart
flutter packages run build_runner build --delete-conflicting-outputs
```

### 36.Container点击区域过小

**GestureDetector 内Container不设置color点击区域会根据内容大小来定**

### 37.xcrun instruments 打开模拟器

xcrun instruments -w "iPhone 8 Plus (13.1)"

### 39. GestureDetector处理手势操作 behavior 行为

- `HitTestBehavior.opaque` **自己处理事件**
- `HitTestBehavior.deferToChild` **child处理事件**
- `HitTestBehavior.translucent` **自己和child都可以接收事件**

### 40.Widget无法居中，对齐



```dart
 Row(
    mainAxisAlignment: MainAxisAlignment.start,
    crossAxisAlignment: CrossAxisAlignment.start,
    children: <Widget>[
          Container(
              width: ScreenUtil().setHeight(114),
              height: ScreenUtil().setHeight(114),
              margin: EdgeInsets.only(
                left: ScreenUtil().setWidth(10),
              ),
              child: Center(child: FailedDot(),),
            )
          : Container()
    ],
  ),
```

### 41.Flutter Container 点击区域太小

使用GestureDetector包裹Container，发现在Container内容为空的区域点击时，捕捉不到onTap点击事件。
 **`解决方案`**：在GestureDetector里面添加属性：**`behavior: HitTestBehavior.opaque,`**即可：



```dart
GestureDetector(
          behavior: HitTestBehavior.opaque,
          child: Container( width: ScreenUtil().setHeight(114),
              height: ScreenUtil().setHeight(114),child:Text('点我')),
          onTap: () {
            this.handlePlayVoice();
          },
        )
```

### 42.监听页面返回事件(返回按钮点击+侧滑返回)

侧滑不会触发onBack回调,因此使用**`WillPopScope`**的`onWillPop`来实现



```dart
 @override
  Widget build(BuildContext context) {
    return WillPopScope(
      onWillPop: () async {
        // 设置草稿箱
        this.setCraft();
        return true;
      },
      child: Container()
  }
```

### 43PageView使用注意事项

**问题描述**：第一次指定加载第二个page，切换时需要切换两次才显示正常

**原因分析**：
 PageView未初始化时默认index = 0,你强行修改时会导致两个index不一致

**解决办法**：



```swift
 _controller = PageController(initialPage: currentIndex);
/// 切换
_controller.animateToPage(
                                  currentIndex,
                                  duration: Duration(
                                    milliseconds:
                                        (pageSwitchAnimatedTime + 100),
                                  ),
                                  curve: Curves.ease,
                                );
```









###  2020年02月28日

-----------------------------------------------------------------





Flexible组件必须是Row、Column、Flex等组件的后裔，并且从Flexible到它封装的Row、Column、Flex的路径必须只包括StatelessWidgets或StatefulWidgets组件(不能是其他类型的组件，像RenderObjectWidgets)。

Row、Column、Flex会被Expanded撑开，充满主轴可用空间。



◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤◢◤

          Navigator.of(context).push(
            MaterialPageRoute(
              builder: (context) => PageA(),
            ),
          );


```java
Navigator.push(context, MaterialPageRoute(builder: (context) {
      return SecondPage();
    }));
```



```dart
    //导航到新路由   
          Navigator.push( context,
           MaterialPageRoute(builder: (context) {
              return NewRoute();
           }));
```



###  2020年02月23日

-----------------------------------------------------------------



### Running the samples

#### iOS / Android

```
cd <sample_directory>
flutter run 
```

#### Web

Make sure you're on Flutter version "Flutter 1.12.13+hotfix.6 • channel beta" or newer. Not all samples support web at this time, so please check the sample directory for a `lib/main_web.dart` file.

```
cd <sample_directory>
flutter run -d chrome -t lib/main_web.dart
```



###  2020年02月23日

-----------------------------------------------------------------

`Flutter GO for web` 的代码库



- git 拉取 `Flutter-go` 项目,并切换到 `web/flutter-go-web-0.0.1` 分支

```
  $ git clone -b web/flutter-go-web-0.0.1 https://github.com/alibaba/flutter-go.git flutter-go-web
```

- 安装flutter_web构建工具

```
  $ flutter pub global activate webdev
```

- 更新pub[**包**]()

```
  $ pub get

  //... 
  Resolving dependencies... 
Warning: You are using these overridden dependencies:
! flutter_web 0.0.0 from git https://github.com/flutter/flutter_web at 6cabfc in packages/flutter_web
! flutter_web_test 0.0.0 from git https://github.com/flutter/flutter_web at 6cabfc in packages/flutter_web_test
! flutter_web_ui 0.0.0 from git https://github.com/flutter/flutter_web at 6cabfc in packages/flutter_web_ui
Got dependencies!
Precompiling executables... (12.0s)
```

- 开发模式,获取（无状态）热重载 webdev

```
  $ webdev serve --auto restart

  [INFO] Building new asset graph completed, took 2.0s
  [INFO] Checking for unexpected pre-existing outputs. completed, took 1ms
  [INFO] Serving `web` on http://127.0.0.1:8080
  [INFO] Running build completed, took 49.7s
  [INFO] Caching finalized dependency graph completed, took 421ms
  [INFO] Succeeded after 50.1s with 3309 outputs (9338 actions)
```

- 浏览器打开 [http://127.0.0.1:8080](http://127.0.0.1:8080/)
- 发布模式,创建最终编译结果,这将创建一个build目录`index.html`，`main.dart.js`以及使用静态HTTP服务器运行应用程序所需的其余文件。

```
  $ webdev build
```





### 



###  2020年02月21日

-----------------------------------------------------------------

不要使用`pub get`或`pub upgrade`命令来管理你的依赖关系。相反，应该使用`flutter packages get`或`flutter packages upgrade`。如果您想手动使用pub，则可以通过设置`FLUTTER_ROOT`环境变量来直接运行它。

## 升级 Flutter channel 和 packages

要同时更新Flutter SDK和你的依赖包，在你的应用程序根目录（包含`pubspec.yaml`文件的目录）中运行`flutter upgrade` 命令:

```shell
$ flutter upgrade
```

## 升级你的依赖包

如果您修改了`pubspec.yaml`文件，或者只想更新应用依赖的包(不包括Flutter SDK)，请使用以下命令：

- `flutter packages get`获取`pubspec.yaml`文件中列出的所有依赖包
- `flutter packages upgrade` 获取`pubspec.yaml`文件中列出的所有依赖包的最新版本





###  2020年02月21日

-----------------------------------------------------------------



要查看您当前使用的分支，请运行`flutter channel`查看。

要切换分支，请使用`flutter channel beta` 或 `flutter channel master`



flutter run --release --verbose






    1、本地Flutter SDK 版本 1.9.1+hotfix.6 。
    2、pubspec.yaml 中的第三方包版本和 pubspec.lock 中的是否对应的上ps 1.12.x 版本请切换到 dev_next 分支



试一试下面这行代码切换到dev分支
`flutter channel dev`
然后
`flutter version`
打印出所有版本
选择其中某个版本,进行切换，比如
`flutter version v1.7.8+hotfix.4`



flutter doctor -v






    $ flutter channel
      Flutter channels:
        *   stable
            beta
            dev
            master
```

flutter pub get

packages get
packages upgrade
flutter upgrade
flutter clean
```


 flutter go，官方的指南版本如下：
1.版本version/channel切换问题

```
    flutter channel beta
    flutter version v1.7.8 + hotfix.4
 

	flutter pub cache repair
    
    flutter channel dev_next 
    flutter version 1.9.1+hotfix.6
    
```

2.将项目适配到web端
```
	flutter create .
```
3.运行到web上 && 运行到android上

```
    flutter run -d chrome
    flutter run -d android
```





###  2020年02月16日

-----------------------------------------------------------------

常用命令

1.编译：

​		flutter packages get: 获取flutter packages包

2.运行：

​		flutter run （默认为debug环境）
​		flutter run --release (以release模式运行)

3.安装

​		帮助：flutter -h 或 flutter --help
​		诊断flutter：flutter doctor
​		查看flutter版本号：flutter --version
​		flutter升级：flutter upgrade

4.打包apk包：

​		直接打包： flutter build apk
​		64位-release： flutter build apk --release --target-platform android-arm64
​		32位-release： flutter build apk --release --target-platform android-arm



编译、运行、发布

```
git clone https://github.com/creatint/light
flutter pub cache repair
flutter packages get
flutter packages upgrade
flutter run
flutter build apk --release
```

Gradle 配置国内阿里云的maven库地址


```

    buildscript {  
      repositories {   
         maven { url 'https://maven.aliyun.com/repository/google' } 
         maven { url 'https://maven.aliyun.com/repository/jcenter' }  
         maven { url 'http://maven.aliyun.com/nexus/content/groups/public' } 
      }  
      dependencies {  
          classpath 'com.android.tools.build:gradle:3.5.3'              
   
       }
    }
    allprojects { 
       repositories {  
          maven { url 'https://maven.aliyun.com/repository/google' }  
          maven { url 'https://maven.aliyun.com/repository/jcenter' }  
          maven { url 'http://maven.aliyun.com/nexus/content/groups/public' }  
          }
    }

```





### 几个flutter常用命令

以下是常用命令：

| 常用命令             | 含义                                    |
| -------------------- | --------------------------------------- |
| **--version**        | 查看Flutter版本                         |
| **-h**或者**--help** | 打印所有命令行用法信息                  |
| analyze              | 分析项目的Dart代码。                    |
| **build**            | Flutter构建命令。                       |
| channel              | 列表或开关Flutter通道。                 |
| clean                | 删除构建/目录。                         |
| config               | 配置Flutter设置。                       |
| **create**           | 创建一个新的Flutter项目。               |
| **devices**          | 列出所有连接的设备。                    |
| **doctor**           | 展示了有关安装工具的信息。              |
| drive                | 为当前项目运行Flutter驱动程序测试。     |
| format               | 格式一个或多个Dart文件。                |
| fuchsia_reload       | 在Fuchsia上进行热重载。                 |
| **help**             | 显示帮助信息的Flutter。                 |
| **install**          | 在附加设备上安装Flutter应用程序。       |
| logs                 | 显示用于运行Flutter应用程序的日志输出。 |
| packages             | 命令用于管理Flutter包。                 |
| precache             | 填充了Flutter工具的二进制工件缓存。     |
| run                  | 在附加设备上运行你的Flutter应用程序。   |
| screenshot           | 从一个连接的设备截图。                  |
| stop                 | 停止在附加设备上的Flutter应用。         |
| test                 | 对当前项目的Flutter单元测试。           |
| trace                | 开始并停止跟踪运行的Flutter应用程序。   |
| **upgrade**          | 升级你的Flutter副本。                   |



 ###  学习随笔
-----------------------------------------------------------------

