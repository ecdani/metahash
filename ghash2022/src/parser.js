const fs = require('fs');

exports.parse = filename => {
  console.log(`- Parsing "${filename}" -`);

  const content = fs.readFileSync(`input/${filename}`, 'UTF-8');
  const lines = content.split(/\n/);

  // TODO: real parsing here...

  return {};
}
