FROM python:3.10.7
LABEL maintainer="yura.vataschuk@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR myapp/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]