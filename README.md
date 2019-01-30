# 报告合成

## 特点
1. 支持Windows、Linux、Docker、GitLab CI
2. 支持中文名称/路径PDF文件合并
3. 自动生成目录页和页眉页脚

## 环境
- TexLive (最好是用Texlive-full) + latexmk + LyX
- Python 2/3 + Jinja
- 中文语言环境（系统/Texlive）
- 操作系统最好用Ubuntu等Linux发行版，以避免Windows环境存在中文编码问题，如果是使用LyX则可以避免编码问题。

## 编译方案一
1. 使用Lyx生成基础模板，并导出tex文件；
2. 使用Latex、Jinja2、Python合成报告(merge.py)。
``` bash
# 示例
python merge.py --dirname="example" --title="Example Reports" --author="Example Author"
latexmk -view=none ./build/example.tex
```

**Note:** Windows下因为中文编码问题导致不能编译成功；文件路径上尽量不要存在下划线。

## (推荐) 编译方案二
使用Lyx生成基础模板,直接用Jinja2、Python合成报告(merge_lyx.py)。
``` bash
# 示例
python merge_lyx.py --dirname="example" --title="Example Reports" --author="Example Author"
lyx --export pdf4 ./build/example.lyx
**Note:** 文件路径上尽量不要存在下划线。
```

## 部署方案一
利用GitLab CI和GitLab Runner

## 部署方案二
利用Docker
```
# 构建镜像
docker build -t merge_reports ./

# 使用编译方案一，使用Git Bash
export DIRNAME="example"
export TITLE="Example Reports"
export AUTHOR="Example Author"
docker run --rm   -v /"$(pwd)/":/merge-technical-reports merge_reports  python3 merge.py --dirname="$DIRNAME" --title="$TITLE" --author="$AUTHOR"
export  TEX_NAME="./build/"$DIRNAME".tex"
docker run --rm   -v /"$(pwd)/":/merge-technical-reports merge_reports  latexmk -view=none "$TEX_NAME"
   
# (推荐) 使用编译方案二
export DIRNAME="example"
export TITLE="Example Reports"
export AUTHOR="Example Author"
docker run --rm   -v /"$(pwd)/":/merge-technical-reports merge_reports  python3 merge_lyx.py --dirname="$DIRNAME" --title="$TITLE" --author="$AUTHOR"
export  LYX_NAME="./build/"$DIRNAME".lyx"
docker run --rm   -v /"$(pwd)/":/merge-technical-reports merge_reports  lyx --export pdf4 "$LYX_NAME"
```
