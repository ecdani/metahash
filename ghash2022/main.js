const fs = require('fs');
const problem = require('./src/problem.js');

const dir = './input/';
fs.readdir(dir, (err, files) => {
  if (err) {
    throw err;
  }

  const start_time = Date.now();
  files.forEach(filename => {
    // Ignore .gitkeep file
    if (filename.startsWith('.')) {
      return;
    }

    problem.resolve(filename);
  });
  const end_time = Date.now();

  console.log(`Processed all files in ${(end_time - start_time) / 1000} seconds`);
});
