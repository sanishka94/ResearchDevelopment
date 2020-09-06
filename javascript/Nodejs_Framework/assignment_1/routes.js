const { title } = require("process");

let htmlIndex = '<html>' +
        '<header><title>Assignment 1</title></header>' +
        '<body>' +
            '<h1>Welcome to my assignment 1</h1>' +
            '<form action="create-user" method="POST">' +
            '<input type="text" name="username">' +
            '<button type="submit">Register</button>' +
            '</form>' +
        '</body>' +
    '</html>';

const htmlUsers = '<html>' +
        '<header><title>Assignment 1</title></header>' +
        '<body>' +
            '<h1>Welcome to my assignment 1</h1>' +
            '<ul>' +
                '<li>User 1</li>' +
                '<li>User 2</li>' +
                '<li>User 3</li>' +
                '<li>User 4</li>' +
                '<li>User 5</li>' +
            '</ul>'+
        '</body>' +
    '</html>';

const requestHandler = (req, res) => {
    const url = req.url;
    if (url === '/') {
        res.setHeader('Content-Type', 'text/html');
        res.write(htmlIndex);
        return res.end();
    }
    if (url === '/users'){
        res.write(htmlUsers);
        return res.end();
    }
    if (url === '/create-user') {
        const body = [];
        req.on('data', (chunk) => {
            body.push(chunk);

        });
        req.on('end', () => {
            const parsedBody = Buffer.concat(body).toString();
            let username = parsedBody.split("=")[1];
            // console.log(`The username is :$(username)`);
            console.log(username);
        });
        res.statusCode = 302;
        res.setHeader('Location', '/users');
        res.end();
    }
};


module.exports = {
    handler: requestHandler
}


