const { connect } = require("http2");
const { rejects } = require("assert");

// This is an object
const person = {
    name: 'Sani',
    age: 26,

    // This function is bounded to the object
    greet() {
        console.log('hi, I am ' + this.name);
    }

    // This function is referencing the global scope
    // greet: () => {
    //     console.log('Hi, I am ' + this.name);
    // }
};

// console.log(person);
// person.greet();


// Arrays
const hobbies = ['Sports', 'Cooking'];
// for (let hobby of hobbies){
//     console.log(hobby);
// }

// console.log(hobbies.map(hobby => 'Hobby: ' + hobby));


// Spread operator
const copiedHobbies = [...hobbies];

// console.log(copiedHobbies);
// console.log(hobbies);

// This is the rest opearator
const toArray = (...args) => args;

// console.log(toArray(1, 2, 3, 4, 'hello'));


// Object destructuring

const printName = ({ name, age }) => name + age;

// console.log(printName(person));

const { name, age } = person;

const [hobby1, hobby2] = hobbies;

// console.log(hobby1);


// Async

// const fetchData = callback => {
//     setTimeout(() => {
//         callback('Done');
//     }, 1500);
// };

const fetchData = () => {
    const promise = new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve('Done');
        }, 1500);
    });
    return promise;
};

setTimeout(() => {
    console.log('Timer is done');
    fetchData().then(text => {
        console.log(text);
    });
}, 2000);


