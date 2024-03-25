RedisOptions option = new RedisOption().setPort(6379).setHost(localhost);
Redis redisClient = new Redis.createClient(vertx, options);

final static String REDIS_PREFIX = "user";
final int userId = 1;
final String redisKey = String.format("%s:%s", REDIS_PREFIX, userId);
redisClient.set(redisKey, "true");


public Future<Option<T>> computeIfAbsent(String key, Supplier<Future<T>> mappingFunction) {
    return cache.get(key)
        .recover(
            return Future.succeeded(Option.none());
        )
        .compose(result -> {
            if (result.isEmpty) {
                return computeSet(key, mappingFunction);
            }
            return result.get()
        })
}
