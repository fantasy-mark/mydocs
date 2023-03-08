### 创建项目

```bash
   3 pip install mkdocs mkdocs-material
   # 创建项目
   5 mkdocs new my-project
   # 添加主题 name: material
   8 notepad.exe .\mkdocs.yml
  13 mkdocs serve
  15 git init .
  16 git remote add origin https://gitee.com/git4mark/docs.git
  19 git add .
  20 git commit -m "1st build"
  24 git push --set-upstream origin master
  25 git push
  # 此操作是推送到gh-pages分支，必须这么做！
  26 mkdocs.exe gh-deploy
```

### gitee设置

> 项目页面-》服务标签-》Gitee Pages打开配置

### 文档配置

[yaml](https://blog.csdn.net/m0_63203517/article/details/127444446)

[mkdocs](https://ai.aianaconda.com/blog/mk-syntax/appendix/yml/)

* 左侧导航条

```yaml
nav:
  - 一. 介绍: index.md
  - 二. 安装:
      - 1. 本地环境搭建: install/local.md
      - 2. 发布至GitHub Pages: install/github-pages.md
      - 3. 发布至自己的HTTP Server: install/http-server.md
  - 三. 语法:
      - 1. 语法总览: syntax/main.md
      - 2. 标题: syntax/headline.md
      - 3. 段落: syntax/paragraph.md # (1)
```

### 进阶（搭配drawio）

[参考](https://www.cnpython.com/pypi/mkdocs-drawio-exporter)

* [安装](https://github.com/jgraph/drawio-desktop/releases)

```bash
pip install mkdocs-drawio-exporter
```

* 配置

1）需要安装draw.io且配置环境变量到PATH

2）draw文件路径不能包含中文

3） yaml文件中配置

```yaml
plugins:
    - search # built-in search must be always activated
    - drawio-exporter
```

* 使用

```markdown
![My alt text](my-diagram.drawio)
# 多页
![Page 1](my-diagram.drawio#0)
```

