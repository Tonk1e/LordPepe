FROM python:3
MAINTAINER ttt0nkle@gmail.com
RUN apt-get install -y libffi-dev
RUN apt-get install -y git
RUN apt-get install -y ffmpeg
WORKDIR /
ADD requirements.txt /requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade -r requirements.txt
ADD . /
CMD ["python", "bot.py"]
