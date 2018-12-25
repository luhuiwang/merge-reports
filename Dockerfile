FROM andlinger/docker-lyx-xelatex:latest
LABEL Name=merge-technical-reports Version=2018.12
RUN apt clean &&\
    sed -i 's/archive.ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list &&\
    apt update --fix-missing &&\
    apt install -qy texlive-publishers texlive-publishers-doc texlive-lang-chinese python3-jinja2 latexmk &&\
    apt install --reinstall -y locales &&\
    sed -i 's/# zh_CN.UTF-8 UTF-8/zh_CN.UTF-8 UTF-8/' /etc/locale.gen  &&\
    rm -rf /var/lib/apt/lists/* 
ENV LANG=zh_CN.UTF-8
ENV LANGUAGE=zh_CN
ENV LC_ALL=zh_CN.UTF-8
RUN dpkg-reconfigure --frontend noninteractive locales

WORKDIR /merge-technical-reports

CMD [ "/bin/bash"]
