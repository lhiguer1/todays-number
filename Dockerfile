FROM python:3.10

ENV PORT=5000
EXPOSE $PORT
WORKDIR /usr/src/app/

COPY . .
RUN pip install --user --no-cache-dir -r requirements.txt &&  \
    python manage.py collectstatic --no-input && \
    python manage.py makemigrations && \
    python manage.py migrate
CMD python manage.py runserver 0.0.0.0:$PORT
