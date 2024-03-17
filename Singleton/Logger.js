class Logger {
    constructor(){
        this.logger;
        this.name = "logger" + Date.now();
    }

    static getInstance() {
        if (!this.logger) {
            this.logger = new Logger();
        }
        return this.logger;
    }

    log(message) {
        console.log("[INFO] message from" + this.name);
    }
}

const logger1 = Logger.getInstance();
const logger2 = Logger.getInstance();

logger1.log("message");
// [INFO] message fromlogger1710606987529
logger2.log("message");
// [INFO] message fromlogger1710606987529