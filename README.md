<div align="center">

<p align="center">
  <a href=""><img src="https://img1.baidu.com/it/u=3563761161,679242917&fm=253&fmt=auto&app=138&f=PNG?w=360&h=360" width="200" height="200" alt="kfc"></a>
</p>

# nonebot_plugin_sky

_✨ 基于 [NoneBot2](https://v2.nonebot.dev/) 的光遇每日攻略插件 ✨_

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/nonebot-2.0.0b4+-red.svg" alt="NoneBot">
  <a href="https://pypi.org/project/nonebot-plugin-sky/">
    <img src="https://badgen.net/pypi/v/nonebot-plugin-sky" alt="pypi">
  </a>
</p>

_“因光而遇”_

</div>

# 目录：

### 1.开始使用

### 2.使用命令

### 3.新版数据包说明

### 4.TODO

### 5.效果图

### 6.遇到问题

### 7.更新日志

# ✨开始使用✨

## 在.env文件中配置接收小助手消息的群号

`recv_group_id="12345"`(单个)

`recv_group_id=["12345","66666",...]`(多个)

## 安装前置插件依赖（**必需**）：

apscheduler:
[Github项目地址](https://github.com/nonebot/plugin-apscheduler)

或 使用nb-cli：

`nb plugin install nonebot_plugin_apscheduler`

## 配置bot.py文件（必需）

您必须确保您的bot.py配置中定时器默认关闭状态，即添加：

`nonebot.init(apscheduler_autostart=False)`

## 安装本插件

1.使用pip包管理器安装(推荐)：

`pip install nonebot-plugin-sky`

或

2.克隆本项目到本地，在bot.py中导入插件：

`nonebot.load_plugin(r"nonebot_plugin_sky")`

# ✨使用命令✨

在有bot的群内发送`[命令前缀]+光遇`或`[命令前缀]+sky`来获取菜单

_当前版本包含的命令_：

| 命令                  | 说明                            |
|---------------------|-------------------------------|
| `sky`/`光遇菜单`        | 获取菜单（列出指令列表）                  |
| `sky -cn`/`今日国服`    | 获取今日国服攻略                      |
| `sky -in`/`今日国际服`   | 获取近日国际服攻略                     |
| `queue`/`排队`        | 获取服务器排队状态                     |
| `notice`/`公告`       | 获取光遇国服官方公告                    |
| `-t 启动`/`小助手启动`     | 启动定时任务并开启雨林干饭小助手              |
| `-t 关闭`/`小助手关闭`     | 关闭定时任务并关闭雨林干饭小助手              |
| `-t 状态`/`小助手状态`     | 查询当前小助手运行状态                   |
| `return -cn`/`国服复刻` | 查询最近的国服复刻先祖                   |
| `开启/关闭转发模式`         | 开启和关闭全局消息转发形式                 |
| `开启/关闭艾特全体`         | 开启和关闭雨林干饭小助手的艾特全体消息           |
| `安装数据包`             | 安装光遇相关攻略的静态资源数据包              |
| `菜单v2`              | 查看数据包的文件名注入命令，这些命令都需要遵循命令前缀规则 |

### 注意：转发模式是默认开启的。在这个状态下部分命令在私聊的环境下没有效果，是因为转发消息不支持私聊。

### 若有需要，关闭转发模式即可。

### **//【攻略数据来自微博@今天游离翻车了吗 @旧日与春 @光遇陈陈】**

### **任何情况下攻略最后的版权信息请勿私自移除**

## ✨★★新版数据包说明★✨

在2.0版本中引入了光遇数据包（SkyDataPack）系统

### 特性：

1.数据包完全独立，与代码互相依存但互不干扰

2.安装后即可立即使用，无需重启NoneBot

3.支持自定义修改或扩充

### 使用教程：

1.在群聊内或私聊bot发送`安装数据包`即可开始下载安装数据包

2.提示安装成功即可开始使用。发送命令`菜单v2`即可查看当前数据包内所有命令

3.自定义方法：数据包的安装路径为：你的Nonebot根目录下`的/SkyDataPack`文件夹

该文件夹的所有子文件夹即为‘命令’文件夹，每个‘命令’文件夹下的所有图片为命令成功执行需要发送的对象。

新建一个命令文件夹，命名为你想设置的命令语句，将要发送的图片对象放入此文件夹内即可。

空文件夹可能会报错，后续修复

***注意***：

1.命令只能为SkyDataPack文件夹内的文件夹，暂不支持子命令和更多极的文件夹

2.命令文件夹下目前只支持图片文件（jpg，png，bmp）

## ✨TODO？✨

* [X]  每日干饭提醒小助手
* [X]  更多光遇攻略
* [ ]  数据包扩充
* [ ]  光遇扩展插件

# ✨效果展示✨

![](.README_images/test.jpg)

# ✨遇到问题✨

## **联系他 （本插件的真寻移植版开发者）**

## **QQ：1179514075**

## **或者联系我本人（优先找他）**

<p align="center">
  <a href="https://github.com/"><img src="https://github.com/Kaguya233qwq/nonebot_plugin_alicdk_get/blob/main/.README_images/17623ac4.png?raw=true" width="300" height="350" alt="QRCode"></a>
</p>

## ✨更新日志✨

2023.1.2 v2.0.3

1.新增国际服复刻

2.修复数据包中发送无关命令仍会报错的问题

3.修复文件无法删除拒绝访问的问题

4.补充部分命令匹配

5.修改数据包命令为精准匹配而不是模糊匹配

6.修改菜单图路径

2022.12.30 v2.0.2

适配linux端

2022.12.30 v2.0.1

1.修复数据包菜单重复追加的问题

2.菜单升级为图片版

2022.12.30 v2.0

新增数据包系统，拥有较好扩展性，支持自定义

2022.12.22 v1.2.10

1.更换国服复刻先祖的数据源

2.小助手支持多个群异步发送定时消息

2022.12.12 v1.2.9

修改国服复刻先祖的数据源

2022.12.10 v1.2.8

新增小助手艾特全体开关

2022.12.5 v1.2.7

修复setups文件及打包

2022.12.5 v1.2.6

新增配置文件，新增全局消息转发配置，支持命令开关

2022 12.3 v1.2.5

修复雨林干饭小助手linux环境下的路径识别问题。

2022 12.2 v1.2.4

修复复刻先祖的搜索逻辑

2022 12.2 v1.2.3

新增国服复刻先祖查询

<details>

<summary>更早的记录（2022.12.1之前）</summary>

<pre><code>

2022 11.28 v1.2.2

移除小助手时间测试脏数据

2022 11.27 v1.2.1

修复雨林干饭小助手无法发送到群的问题

2022 11.22 v1.2.0

新增雨林干饭小助手（国服时间，国际服暂不考虑）开启后每到饭点提前五分钟自动提醒

2022 11.21 v1.1.5

取消消息转发机制规避部分账号风控问题

2022 11.19 v1.1.4

修复pypi打包不全问题

2022 11.18 v1.1.3

修复国际服攻略解析失败的问题

2022.11.18 v1.1.1

新增获取公告命令

2022.11.18 v1.1

1.重构项目结构

2.新增国际服今日攻略

3.新增排队人数查询

4.新增菜单命令

2022.11.14 v1.0.4

修复已知问题

2022.11.14 v1.0.3

修复当bot的昵称配置为空时获取的数据为空记录的问题

2022.11.14 v1.0.2

修复当游离未将今日攻略顶置时获取不到数据的问题

2022.11.5 v1.0.1

1.将结果用聊天记录转发的形式展现

2.修复已知问题

2022.11.3 v1.0

初推版本

</code></pre>

</details>

