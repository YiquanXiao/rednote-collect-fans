# RedNote Collect Fans

**This README includes both English and 中文 versions.**  
**Click to jump to: [English Version](#english-version) | [中文说明](#中文说明)**

---

## English Version

### Overview

**RedNote Collect Fans** is an automation script using [uiautomator2](https://github.com/openatx/uiautomator2) to collect follower IDs from a Xiaohongshu (RED) user and save them into a CSV file.

### Features

- Launch Xiaohongshu app on Android
- Search for a target user
- Open their follower list
- Scroll through and extract each follower’s unique ID
- Save all IDs (de-duplicated) to a local CSV file

### Requirements

- Python 3.x
- `uiautomator2`
- `pandas`

Install dependencies:

```bash
pip install uiautomator2 pandas
````

### How to Use

1. **Connect Android device** (enable USB debugging) and initialize:

```bash
python3 -m uiautomator2 init
```

2. **Edit the script** to set your target user ID:

```python
if __name__ == '__main__': 
    get_xhs_follower_ids(user_id="114765256", max_scroll=10)
```

3. **Run the script**:

```bash
python RedNote_collect_fans.py
```

The script will save a CSV file named `{user_id}.csv` with all collected follower IDs.

### Notes

* Includes random sleep to simulate human behavior and avoid bot detection.
* Stops early if no new followers are found during scrolling.
* Works best on the latest Xiaohongshu app.
* **For educational use only. Use responsibly.**

---

## 中文说明

### 简介

**RedNote Collect Fans** 是一个基于 [uiautomator2](https://github.com/openatx/uiautomator2) 的自动化脚本，用于采集小红书用户的粉丝 ID 并导出为 CSV 文件。

### 功能

* 启动 Android 上的小红书应用
* 搜索目标用户
* 打开其粉丝列表
* 滚动页面，进入每个粉丝主页获取其唯一 ID
* 去重后导出所有 ID 到本地 CSV 文件

### 环境依赖

* Python 3.x
* `uiautomator2`
* `pandas`

安装依赖：

```bash
pip install uiautomator2 pandas
```

### 使用方法

1. **连接 Android 设备**（开启 USB 调试）并初始化：

```bash
python3 -m uiautomator2 init
```

2. **编辑脚本**中的 user\_id：

```python
if __name__ == '__main__': 
    get_xhs_follower_ids(user_id="114765256", max_scroll=10)
```

3. **运行脚本**：

```bash
python RedNote_collect_fans.py
```

脚本完成后会在当前目录生成一个名为 `{user_id}.csv` 的粉丝ID列表文件。

### 注意事项

* 使用随机延迟模拟人类操作，降低被识别为机器人风险；
* 若连续未发现新粉丝ID，将提前退出循环；
* 建议使用最新版小红书应用；
* **本脚本仅供学习研究使用，使用时请遵守相关平台规则。**
