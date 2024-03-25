writer
    .newQuery(SELECT_EXISTING_HEARTBEAT)
    .execute(params)
    .map(result -> {
        if (result.totalRows() == 0) {
            return Optional.empty();
        }
        return Optional.of(row.first.get());
    })
    .compose(optionalHeartbeat -> {
        if (optionalHeartbeat.isEmpty()) {
            return writer.newQuery(INSERT)
        } else {
            return writer.newQuery(UPDATE)
        }
    })
    .onComplete(res -> {
        if (res.failed()) {
            res.rollback();
        } else {
            res.commit();
        }
    }