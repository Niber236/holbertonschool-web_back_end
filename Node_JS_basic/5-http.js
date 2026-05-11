const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');
    try {
      // On intercepte le console.log pour l'envoyer dans la réponse HTTP
      const oldLog = console.log;
      let output = '';
      console.log = (msg) => { output += `${msg}\n`; };
      
      await countStudents(process.argv[2]);
      
      console.log = oldLog;
      res.end(output.trimEnd());
    } catch (error) {
      res.end('Cannot load the database');
    }
  }
});

app.listen(1245);
module.exports = app;