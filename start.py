import redis

# Connect to Redis
r = redis.from_url('rediss://red-cmf1m5qcn0vc73buq2e0:KM5M3jT3x8Ndz5NsLcmyeCdWHd66RKCM@oregon-redis.render.com:6379')

# Set a key-value pair
# r.set('mykey', 'Hello, Redis!')
value = r.get('mykey')
print(value)