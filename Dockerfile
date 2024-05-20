FROM python:3.12.3-bullseye

RUN mkdir -p /home/Tachyon

COPY . /home/Tachyon

WORKDIR /home/Tachyon

RUN pip install -r requirements.txt

CMD ["python", "maximon.py"]