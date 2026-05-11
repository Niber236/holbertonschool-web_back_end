const fs = require('fs').promises;

const countStudents = (path) => fs.readFile(path, 'utf8')
  .then((data) => {
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1);
    console.log(`Number of students: ${students.length}`);

    const fields = {};
    for (const line of students) {
      const [firstname, lastname, age, field] = line.split(',');
      if (!fields[field]) fields[field] = [];
      fields[field].push(firstname);
    }

    for (const field in fields) {
      console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
    }
  })
  .catch(() => {
    throw new Error('Cannot load the database');
  });

module.exports = countStudents;
