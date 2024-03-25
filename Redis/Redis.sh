# docker run --name my-redis-container -d -p 6379:6379 redis

SET user:1 true

GET user
# (nil)

GET user:1
# "true"

# Add a set of values
SADD group 1 2 3
# (integer) 3

SMEMBERS group
# 1) "1"
# 2) "2"
# 3) "3"

SISMEMBER group 1
# (integer) 1
SISMEMBER group 5
# (integer) 0

SREM group 1
# (integer) 1

KEYS *
# 1) "group"
# 2) "user:1"

KEYS user
# (empty array)

KEYS user*
# 1) "user:1"

DEL group