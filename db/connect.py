import os
import redis
import sqlalchemy
from os import environ
from dotenv import load_dotenv
load_dotenv()


def init_redis_pool():
    redis_host = "redis-17091.c259.us-central1-2.gce.cloud.redislabs.com"
    redis_port = 17091
    redis_pass = "xkVYgSOVSCW6TctTKxzER2t1MH9VTq61"
    pool = redis.ConnectionPool(
        host=redis_host,
        port=redis_port,
        password=redis_pass,
        db=0)
    return pool


redis_client = redis.Redis(connection_pool=init_redis_pool())
