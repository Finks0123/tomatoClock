# 番茄闹钟

:tomato: 一个让你专注工作的番茄闹钟，


## 项目说明

该项目融合RunCat项目和自制番茄闹钟，使用wxPython开发。

## 运行

直接运行main.py即可



## 打包说明

本项目使用pyinstller打包，需要解决连个问题：

1. 打包程序过大
2. 如何加入外部资源进行打包



### 1、如何解决pyinstaller程序打包后过大的问题：

> 参考 [使用pipenv建立虚拟环境解决python打包exe文件过大的问题（附打包带图标，多个py文件打包exe）]( https://blog.csdn.net/KOBEYU652453/article/details/108710837)

解决流程如下：

1）安装pipenv,并进入虚拟环境

```
pip install pipenv
```

```
pipenv shell
```

2）安装程序运行需要的包。建议先建一个requirement。本程序只要安装wxPython

```
pip install wxPython
```

3）测试运行, 能否跑通

`python main.py`

4）安装pyinstaller并开始打包

```
pip install pyinstaller
```

```
pyinstaller -F .\main.py -w -i .\data\img.ico
```

说明：

-F 生成一个exe文件

-w 关闭命令行

-i 自定义程序图标

但是打包完发现外部资源路径错误。来到第二个问题，如何打包外部资源到exe中

### 2、 如何打包外部资源

参考： [博客](https://blog.csdn.net/kobeyu652453/article/details/108732747?ops_request_misc=&request_id=&biz_id=102&utm_term=%E8%AF%BB%E5%8F%96%E6%96%87%E4%BB%B6%E5%A4%B9%E5%9B%BE%E7%89%87%E7%9A%84%E7%A8%8B%E5%BA%8F%E6%80%8E%E4%B9%88%E6%89%93%E5%8C%85%E6%88%90exe&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-4-108732747.142^v20^pc_rank_34,157^v15^new_3&spm=1018.2226.3001.4187)

1）修改程序中的目录，注意程序中的目录一定要用绝对目录，而且是计算得到的绝对目录，不然容易出错， 如下这样写就行了。

```python
if getattr(sys, 'frozen', False): #是否Bundle Resource
    app_path = sys._MEIPASS
else:
    app_path = os.path.dirname(os.path.abspath(__file__))

# 具体绝对目录
path = os.path.join(app_path, 'img.png')
```

2）修改spec文件

执行上述4步骤后发现当前目录下生成了一个`.spec`文件 , 打开它，修改资源的目录,  也就是data, 把当前目录下的资源目录加进去，如下。

```
a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[("source","source")],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
```

3）重新打包一下spec

```
pyinstaller main.spec
```



以上就妥了，重新生成的ext就包含资源文件了。
