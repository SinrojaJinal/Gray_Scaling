FROM python:3.6

WORKDIR /usr/src/app

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python","./main.py"]
# ENTRYPOINT ["python", "./main.py"]