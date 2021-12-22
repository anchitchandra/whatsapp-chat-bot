from db.redis_utils import (
    get_from_redis,
    set_into_redis
)


def get_user(senderid, redis_client):
    if redis_client.get(senderid) is None:
        user = {
            'senderid': senderid,
            'pvalue': '0',
            'nextval': 1,
            'registered_id': None
        }

        set_into_redis(senderid, user, redis_client)
    return get_from_redis(senderid, redis_client)


def update_user(senderid, value, redis_client):
    set_into_redis(senderid, value, redis_client)
    return get_from_redis(senderid, redis_client)


def reset_user(senderid, redis_client):
    user = {
        'senderid': senderid,
        'pvalue': '0',
        'nextval': 1,
        'registered_id': None
    }
    set_into_redis(senderid, user, redis_client)
    return get_from_redis(senderid, redis_client)
