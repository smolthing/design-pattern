class LRUCache2 {
    private capacity: number;
    private cache: Map<number, number>;
    private queue: any[];

    constructor(capacity: number) {
        this.cache = new Map(); // cache allows key to be different types, object only allows string as key
        this.capacity = capacity;
        this.queue = [];
    }

    get(key: number): number | undefined {
        if (!this.cache.has(key)) {
            return -1;
        }

        this.moveToNewest(key);
        return this.cache.get(key);
    }

    put(key: number, value: number): void {
        if (this.cache.has(key)) {
            this.removeKey(key);
        } else if (this.queue.length >= this.capacity) {
            this.removeOldest();
        }

        this.cache.set(key,value);
        this.queue.push(key);
    }

    removeKey(key: number): void {
        const index = this.queue.indexOf(key);
        this.queue.splice(index, 1);
    }

    moveToNewest(key: number): void {
        this.removeKey(key);
        this.queue.push(key); // add to back, use shift to remove first, splice to take out index
    }

    removeOldest(): void {
        const key = this.queue.shift();
        this.cache.delete(key);
    }

    print(): void {
        this.queue.forEach(key => console.log(key + "=>" + this.cache.get(key)));
    }
}

const cache2 = new LRUCache2(3);
cache2.put(1,10);
cache2.put(2,20);
cache2.put(3,30);
cache2.get(1);
cache2.put(2,200);
cache2.print(); //3:30, 1:10, 2:200