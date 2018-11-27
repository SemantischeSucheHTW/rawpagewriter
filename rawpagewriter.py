from rawpagedao import MongoDBDao
from rawpagesource import KafkaSource

from parseorder import ParseOrder
from parseordersink import KafkaSink

import os


def env(key):
    value = os.environ.get(key)
    if not value:
        raise f"{key} not set!!!"
    return value

rawPagesKafkaSourceConfig = {
        "topic": env("KAFKA_RAWPAGES_TOPIC"),
        "bootstrap_servers": env("KAFKA_BOOTSTRAP_SERVERS"),
        "group_id": env("KAFKA_GROUP_ID")
}

parseOrdersKafkaSinkConfig = {
        "topic": env("KAFKA_PARSEORDERS_TOPIC"),
        "bootstrap_servers": env("KAFKA_BOOTSTRAP_SERVERS"),
}

mongoDBConfig = {
        "host": env("MONGODB_HOST"),
        "db": env("MONGODB_DB"),
        "collection": env("MONGODB_RAWPAGES_COLLECTION"),
        "username": env("MONGODB_USERNAME"),
        "password": env("MONGODB_PASSWORD"),
        "authSource": env("MONGODB_DB")
}

kafkaSource = KafkaSource(rawPagesKafkaSourceConfig)
kafkaSink = KafkaSink(parseOrdersKafkaSinkConfig)
mongoDBDao = MongoDBDao(mongoDBConfig)

err = None
while not err:
    page = kafkaSource.getPage()
    err = mongoDBDao.storePage(page)
    if (err):
        break
    kafkaSink.send(ParseOrder(page.url, page.datetime))

print(f"ERROR during write: {err}")
