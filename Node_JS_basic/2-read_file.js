const fs = require('fs');
const countStudents = (path) => {
  try {
    const data = fs.readFileSync(path, 'utf-8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1);
    console.log(`Number of students: ${students.length}`);

    const fields = {};
    for (const line of students) {
      const [firstname, lastname, age, field] = line.split(',');
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    }
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
