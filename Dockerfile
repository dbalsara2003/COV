FROM python

RUN mkdir -p /usr/src/

WORKDIR /usr/src/

COPY ./app .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["python3", "/usr/src/app/app.py"]
