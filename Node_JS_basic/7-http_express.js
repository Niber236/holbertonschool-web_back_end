const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  let responseText = 'This is the list of our students\n';
  
  // Capture du log
  const oldLog = console.log;
  let output = '';
  console.log = (msg) => { output += `${msg}\n`; };

  try {
    await countStudents(process.argv[2]);
    console.log = oldLog;
    res.send(`${responseText}${output.trimEnd()}`);
  } catch (error) {
    console.log = oldLog;
    res.send(`${responseText}Cannot load the database`);
  }
});

app.listen(port);
module.exports = app;