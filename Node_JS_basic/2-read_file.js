const fs = require('fs');

const countStudents = (path) => {
  try {
    // 1. LIRE le fichier (ce que tu as oublié)
    const data = fs.readFileSync(path, 'utf-8');

    // 2. DÉCOUPER les lignes
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    
    // 3. VIRER l'en-tête et compter
    const students = lines.slice(1);
    console.log(`Number of students: ${students.length}`);

    // 4. TRIER par domaine
    const fields = {};
    for (const line of students) {
      const [firstname, lastname, age, field] = line.split(',');
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    }

    // 5. AFFICHER les résultats (tu avais oublié cette boucle !)
    for (const field in fields) {
      const list = fields[field].join(', ');
      const count = fields[field].length;
      console.log(`Number of students in ${field}: ${count}. List: ${list}`);
    }

  } catch (error) {
    // Si le fichier n'existe pas, on tombe ici
    throw new Error('Cannot load the database');
  }
};

module.exports = countStudents;