// only function have the prototype method

function Con(name, age) {
    this.name = name;
    this.age = age;
}

console.log(Con.__proto__.__proto__ === Object.prototype)

console.log(typeof Object)