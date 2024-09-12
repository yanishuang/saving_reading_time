# 划词助手 Chrome 扩展

## 简介

划词助手是一个强大的 Chrome 浏览器扩展，旨在提高用户的阅读效率和信息处理能力。通过简单的划词操作，用户可以快速获取选中文本的摘要，从而节省阅读时间并提升信息获取效率。

## 主要功能

1. 网页文本选择：用户可以在任何网页上选择感兴趣的文本。
2. 右键菜单集成：通过右键菜单快速访问摘要功能。
3. 弹出窗口展示：在扩展弹出窗口中显示选中的文本和生成的摘要。
4. 一键摘要生成：点击按钮即可获取选中文本的智能摘要。
5. 实时结果展示：在弹出窗口中实时显示生成的摘要结果。

## 技术实现

- 使用 Chrome Extension API 实现浏览器扩展功能。
- 采用 HTML、CSS 和 JavaScript 构建用户界面。
- 后端服务使用 Python Flask 框架开发，提供文本摘要 API。

## 安装指南

### Chrome 扩展安装

1. 克隆本仓库到本地：
   ```
   git clone https://github.com/your-username/saving_reading_time.git
   ```
2. 打开 Chrome 浏览器，进入 `chrome://extensions/`
3. ���启右上角的"开发者模式"
4. 点击"加载已解压的扩展程序"
5. 选择克隆仓库中的 `source` 文件夹

### 服务端部署

1. 进入 `server` 目录：
   ```
   cd saving_reading_time/server
   ```
2. 安装所需的 Python 包：
   ```
   pip install -r requirements.txt
   ```
3. 运行 Flask 应用：
   ```
   python app.py
   ```

服务器将在 `http://127.0.0.1:5000` 上运行。

## 使用方法

1. 在任何网页上选择文本
2. 右键点击，选择"✨ 使用划词助手分析"
3. 点击 Chrome 工具栏中的扩展图标
4. 在弹出的窗口中查看选中的文本
5. 点击"归纳内容"按钮获取文本摘要

## 项目��构

```
saving_reading_time/
├── source/             # Chrome 扩展源代码
│   ├── manifest.json   # 扩展配置文件
│   ├── background.js   # 后台脚本
│   ├── content.js      # 内容脚本
│   ├── popup.html      # 弹出窗口 HTML
│   └── popup.js        # 弹出窗口脚本
├── server/             # 服务器端代码
│   ├── app.py          # Flask 应用主文件
│   └── README.md       # 服务器说明文档
└── README.md           # 项目主说明文档
```

## 贡献

欢迎贡献！如果您有任何改进意见或发现了 