FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /platzigram
WORKDIR /platzigram
COPY requirements.txt /platzigram/
COPY manage.py /platzigram/
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN chmod +x /platzigram/manage.py