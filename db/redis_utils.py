import pickle


def get_from_redis(key, redis_client):
    data = redis_client.get(key)
    if data is None:
        return None
    return pickle.loads(data)


def set_into_redis(key, value, redis_client, ex=None):
    if ex is not None:
        redis_client.set(key, pickle.dumps(value), ex=ex)
        return True
    redis_client.set(key, pickle.dumps(value))
    return True


def set_multi_into_redis(dict, redis_client):
    for k, v in dict.items():
        set_into_redis(k, v, redis_client)
