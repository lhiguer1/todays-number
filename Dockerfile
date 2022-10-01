FROM python:3.10

WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

RUN python manage.py collectstatic --no-input

CMD python manage.py runserver 0.0.0.0:5000
