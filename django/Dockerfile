FROM python:3.9.19-alpine
EXPOSE 8000
WORKDIR /django-server
COPY . .
RUN pip install -r requirements.txt
RUN chmod a+x docker.sh
RUN /django-server/docker.sh
ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
