FROM python:3.12
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY manage.py manage.py
COPY books books
COPY lib_apiv2 lib_apiv2
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]