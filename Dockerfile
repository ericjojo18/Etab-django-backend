FROM python

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install setuptools

COPY . /app

EXPOSE 8000

CMD ["python", "manage.py","runserver", "0.0.0.0:8000"]


