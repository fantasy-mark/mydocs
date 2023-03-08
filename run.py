# _*_ coding: utf-8 _*_
# author: Mark
# contact: hacker.do@163.com
# datetime: 2023/3/4

import os
import platform
import subprocess

SEPARATOR = '\\' if platform.system() == 'Windows' else '/'


def exec_cmd(cmd):
    """
    执行命令
    :param cmd: 命令字符串
    :return: 执行后的输出结果列表
    """
    print(cmd)
    pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    return pipe.stdout.readlines()


def exec_cmd_status(cmd):
    """
    执行命令, 执行错误会抛出异常
    :param cmd: 命令字符串
    :return:
    """
    print(cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    p.communicate()
    assert (p.returncode == 0)


def checkEnv():
    result = exec_cmd(f'pip show mkdocs mkdocs-material  mkdocs-drawio-exporter')
    for line in result:
        if 'not found' in line.decode(encoding='utf8'):
            print(line + ', let us install packages')
            proxy = f'https://pypi.tuna.tsinghua.edu.cn/simple'
            cmd = f'pip install mkdocs mkdocs-material  mkdocs-drawio-exporter -i ' + proxy
            exec_cmd(cmd)
            break


def updateYaml():
    """
    更新yaml文件的导航信息
    """
    nav = 'nav:'
    buffer = ""
    curLev = False
    curDepth = 0

    with open('mkdocs.yml', mode='r', encoding='utf-8') as f:
        lines = f.readlines()  # 读取文件
        for line in lines:
            if not line.startswith(nav):
                buffer += line
            else:
                break

    nav += '\n'
    # 根据目录生成nav
    for curDir, dirs, files in os.walk("docs"):
        dirs[:] = [d for d in dirs if not d == 'drawio-exporter']

        dirLevel = curDir.split(SEPARATOR)[1:]
        depth = len(dirLevel)
        # 因为是bfs, 最多回退一级, 所以只需要回到上级即可
        curLev = (depth == curDepth)
        curDepth = depth
        if depth < 1:
            continue

        if len(files) < 1:
            continue
        for level, name in enumerate(dirLevel, start=1):
            if curLev and level != len(dirLevel):
                continue
            nav += '  ' * level + ' - ' + name + ':\n'
        for name in files:
            if not name.endswith('.md'):
                continue
            nav += '  ' * (depth + 1) + ' - ' + name.split('.')[0] + ': ' + curDir.split('docs' + SEPARATOR)[1] + \
                   SEPARATOR + name + '\n'

    if 'nav\n' == nav:  # 没匹配到任何文档情况
        return

    with open('mkdocs.yml', mode='w', encoding='utf-8') as f2:
        f2.writelines(buffer + nav)


def try2Push():
    exec_cmd(f'git add .')
    result = exec_cmd(f'git status')
    # TODO
    for line in result:
        if line.decode(encoding='utf8').startswith('Changes to be committed'):
            info = input("输入提交信息: ")
            exec_cmd(f'git commit -m "{info}"')
    exec_cmd_status(f'git push')


def runBuild():
    """
    执行构建网页
    """
    mode = input("输入 '', 1, local 本地执行, 输入 2, push 线上发布\n")

    if mode in ['', '1', 'local']:
        exec_cmd_status(f'mkdocs serve')
    elif mode in ['2', 'push']:
        # exec_cmd_status(f'git pull')
        try2Push()
        exec_cmd_status(f'mkdocs gh-deploy')
        print("Serving on https://fantasy-mark.github.io/mydocs/")


if __name__ == '__main__':
    checkEnv()
    updateYaml()
    runBuild()

    input("回车退出...")
