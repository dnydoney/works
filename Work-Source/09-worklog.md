



https://www.paddlepaddle.org.cn/paddlex/download



python pdseg/train.py --cfg configs/unet_optic.yaml  --use_gpu --do_eval --use_vdl  --vdl_log_dir train_log  BATCH_SIZE 4 SOLVER.LR 0.001



```
python pdseg/eval.py --use_gpu --cfg configs/unet_optic.yaml TEST.TEST_MODEL saved_model/unet_optic/final
```



```
python pdseg/eval.py --use_gpu \
                     --cfg configs/unet_optic.yaml \
                     TEST.TEST_MODEL saved_model/unet_optic/final
```

!python pdseg/train.py --cfg configs/unet_optic.yaml \

​           --use_gpu \

​           --do_eval \

​           --use_vdl \

​           --vdl_log_dir train_log \

​           BATCH_SIZE 4 \

​           SOLVER.LR 0.001



智能制造教学设备，新能源汽车教学设备，智慧教室系统，智慧班牌系统，智慧教学系统，微课教学系统，全景录播系统，远程授课系统，实验室管理系统，智能环境检测管理系统，AI智能录播，双屏教学，实验室安全管理系统





request模块：requests是python实现的简单易用的HTTP库，官网地址：

http://cn.python-requests.org/zh_CN/latest/BeautifulSoup



库：

Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库。网址：https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/



https://baike.baidu.com/item/%E9%9D%92%E6%98%A5%E6%9C%89%E4%BD%A0%E7%AC%AC%E4%BA%8C%E5%AD%A3