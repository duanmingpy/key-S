# key-S

运行环境： ![python3.6+](https://img.shields.io/badge/python-3.6+-green.svg?style=plastic)


简介: 在任何编辑器中，它都能够让你通过ECS键 配合 H、J、K、L控制上下左右。


### 安装


1. 下载当前项目到本地:

![下载方式zip](https://github.com/duanmingpy/key-S/blob/author-dev/readme_photos/key-S-download.png)


2. python3环境下：

```shell script
pip3 install pynput
```

3. 解压项目文件


4. 进入项目中`hjkl_tool.py`所在目录：

```shell script
nohup python3 hjkl_tool.py &
```

5. 再次回车



### 使用

进入编辑器使用：

- `esc + h`  等价  `←`
- `esc + j`  等价  `↓`
- `esc + k`  等价  `↑`
- `esc + l`  等价  `→`


### 关闭hjkl_tool

在mac的terminal窗口中执行(windows按照功能相同的命令杀掉即可)：

```shell script
ps
```

查询结果：
```shell script
  PID TTY           TIME CMD
16845 ttys000    0:00.53 -zsh
20039 ttys000    0:00.46 /Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python hjkl_tool.py
```

找到`hjkl_tool.py`运行的进程id，使用kill命令杀掉进程即可

```shell script
kill -9 20039
```



