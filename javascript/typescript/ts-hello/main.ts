import { throws } from "assert";

function log(message) {
    console.log(message);
}
var message = 'Hello world';
log(message);




class Point {
    // x: number;
    // y: number;

    // '?' makes the variables optional
    // constructor(x?:number, y?:number){
    //     this.x = x;
    //     this.y = y;
    // }

    constructor(private _x?: number, private _y?: number) { }

    draw() {
        console.log('X: ' + this.x + ', Y: ' + this.y);
    }

    getX() {
        return this.x;
    }

    setX(value) {
        if (value < 0) {
            throw new Error('Value cannot be less than 0');
        }
        this.x = value;
    }

    get x() {
        return this.x;
    }

    set x(value) {
        if (value < 0) {
            throw new Error('Value cannot be less than 0');
        }
        this.x = value;
    }
}

let point = new Point(1, 2);
let x = point.getX();
point.setX(10);
point.draw();