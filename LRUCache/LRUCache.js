"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
require("core-js"); // Import core-js at the beginning of your file
var LRUCache2 = /** @class */ (function () {
    function LRUCache2(capacity) {
        this.cache = new Map(); // cache allows key to be different types, object only allows string as key
        this.capacity = capacity;
        this.queue = [];
    }
    LRUCache2.prototype.get = function (key) {
        if (!this.cache.has(key)) {
            return -1;
        }
        this.moveToNewest(key);
        return this.cache.get(key);
    };
    LRUCache2.prototype.put = function (key, value) {
        if (this.cache.has(key)) {
            this.removeKey(key);
        }
        else if (this.queue.length >= this.capacity) {
            this.removeOldest();
        }
        this.cache.set(key, value);
        this.queue.push(key);
    };
    LRUCache2.prototype.removeKey = function (key) {
        var index = this.queue.indexOf(key);
        this.queue.splice(index, 1);
    };
    LRUCache2.prototype.moveToNewest = function (key) {
        this.removeKey(key);
        this.queue.push(key);
    };
    LRUCache2.prototype.removeOldest = function () {
        var key = this.queue.shift();
        this.cache.delete(key);
    };
    LRUCache2.prototype.print = function () {
        var _this = this;
        this.queue.forEach(function (key) { return console.log(key + "=>" + _this.cache.get(key)); });
    };
    return LRUCache2;
}());
var cache2 = new LRUCache2(3);
cache2.put(1, 10);
cache2.put(2, 20);
cache2.put(3, 30);
cache2.get(1);
cache2.put(2, 200);
cache2.print(); //3:30, 1:10, 2:200
