const http = require('http');  //without the '/', it will look for a global module
const routes = require('./routes');

// function rqListener(req, res) {} // using an annonymous function instead of this

const server = http.createServer(routes);

// // If the second expoet method is used
// const server = http.createServer(routes.handler);
// console.log(routes.someText);

server.listen(3000);