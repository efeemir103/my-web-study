const express = require('express');
const path = require('path');
const url = require('url');
const app = express();
const port = 8080;

app.get(/\/.*/, (req, res) => {
    console.log(req.url);
    res.sendFile(path.join(__dirname, 'src', req.url));
});

app.listen(port, () => console.log(`Example app listening on port ${port}!`));