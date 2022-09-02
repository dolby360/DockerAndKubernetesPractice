const fs = require('fs');
const express = require('express');
const app = express();

const content = 'Some dd content!';
fs.writeFile('/app/file.txt', content, err => {
  if (err) {
    console.error(err);
  }
});

app.get('/', (req, res) => {
  res.send(`
    <h1>Hello from inside the very basic Node app!</h1>
  `);

})

console.log('The value of SOME_GLOBAL_ENV_VAR is:', process.env.SOME_GLOBAL_ENV_VAR);
console.log('The value of SOME_GLOBAL_ENV_VAR is:', process.env.MY_ARG);

app.listen(3000);

