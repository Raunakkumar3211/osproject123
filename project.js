class GCObject {
    static idCounter = 1;

    constructor(generation = 0) {
        this.id = GCObject.idCounter++;
        this.generation = generation;
        this.refCount = 1;
        console.log(`Object ${this.id} created in generation ${this.generation}`);
    }

    addReference() {
        this.refCount++;
    }

    removeReference() {
        this.refCount--;
        if (this.refCount === 0) {
            console.log(`Object ${this.id} collected from generation ${this.generation}`);
        }
    }
}

class GarbageCollector {
    constructor() {
        this.generations = [[], [], []];
        this.objects = new Map();
    }

    allocate(gen = 0) {
        const obj = new GCObject(gen);
        this.generations[gen].push(obj);
        this.objects.set(obj.id, obj);
        return obj;
    }

    collect(gen) {
        console.log(`\nRunning Garbage Collection for Generation ${gen}`);
        this.generations[gen] = this.generations[gen].filter(obj => {
            if (obj.refCount === 0) {
                this.objects.delete(obj.id);
                return false;
            }
            return true;
        });
    }

    promote(obj) {
        if (obj.generation < 2) {
            console.log(`Promoting Object ${obj.id} to Generation ${obj.generation + 1}`);
            this.generations[obj.generation] = this.generations[obj.generation].filter(o => o !== obj);
            obj.generation++;
            this.generations[obj.generation].push(obj);
        }
    }
}

// Example usage
const gc = new GarbageCollector();
const obj1 = gc.allocate();
const obj2 = gc.allocate();
const obj3 = gc.allocate(1);

obj1.removeReference();
gc.collect(0);

gc.promote(obj2);
gc.collect(1);
