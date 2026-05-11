const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;
const databasePath = process.argv[2];

// Route de base
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Route complexe pour les étudiants
app.get('/students', async (req, res) => {
  // On commence par le titre
  let responseText = 'This is the list of our students\n';

  // RUSE : On intercepte les console.log pour les mettre dans une variable
  const logs = [];
  const oldLog = console.log;
  console.log = (d) => { logs.push(d); };

  try {
    // On attend que la fonction asynchrone finisse son boulot
    await countStudents(databasePath);
    
    // On remet le console.log normal pour ne pas casser le reste du système
    console.log = oldLog;

    // On assemble tout le texte capturé
    responseText += logs.join('\n');
    res.send(responseText);
  } catch (error) {
    // Si ça foire, on remet aussi le console.log normal
    console.log = oldLog;
    res.send(`${responseText}${error.message}`);
  }
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

module.exports = app;
