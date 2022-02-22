const fs = require('fs');

exports.write = filename => {
  console.log(`- Writing "${filename}"" -`);

  // TODO: generate real output here.
  const content = 'Example data';

  fs.writeFile(`output/${filename}`, content, err => {
    if (err) {
      throw err;
    }
  });
}
