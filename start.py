import redis

# Connect to Redis
r = redis.from_url('')

# Set a key-value pair
# r.set('mykey', 'Hello, Redis!')
value = r.get('mykey')
print(value)