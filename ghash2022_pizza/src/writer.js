const fs = require('fs');

exports.write = (filename, ingredients) => {
  console.log(`- Writing "${filename}"" -`);

  let content = ingredients.length;
  content += ' ' + ingredients.join(' ');

  fs.writeFile(`output/${filename}`, content, err => {
    if (err) {
      throw err;
    }
  });
}
