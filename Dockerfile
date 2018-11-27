FROM python:3.7-stretch

RUN mkdir /rawpagewriter
WORKDIR /rawpagewriter

#COPY feedparser-5.2.1.tar.gz .
#COPY kafka-python-1.4.3.tar.gz .
#RUN pip install feedparser-5.2.1.tar.gz kafka-python-1.4.3.tar.gz
RUN pip install kafka-python pymongo

COPY rawpagedao rawpagedao
COPY rawpagedata rawpagedata
COPY rawpagesource rawpagesource
COPY parseorder parseorder
COPY parseordersink parseordersink

COPY rawpagewriter.py .

ENV KAFKA_BOOTSTRAP_SERVERS kafka:9092
ENV KAFKA_GROUP_ID mongowriter


ENV KAFKA_RAWPAGES_TOPIC rawpages
ENV KAFKA_PARSEORDERS_TOPIC parseorders

ENV MONGODB_HOST mongo
ENV MONGODB_DB default
ENV MONGODB_RAWPAGES_COLLECTION rawpages
ENV MONGODB_USERNAME rawpagewriter
ENV MONGODB_PASSWORD rawpagewriter
