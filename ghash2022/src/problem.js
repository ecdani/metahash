const parser = require('./parser.js');
const writer = require('./writer.js');

exports.resolve = filename => {
  const start_time = Date.now();

  let data = parser.parse(filename);

  console.log(`- Resolving "${filename}" -`);

  // TODO: real solving here...

  writer.write(filename.replace('.in','.out'));

  const end_time = Date.now();
  console.log(`Processed "${filename}" in ${(end_time - start_time) / 1000} seconds`);

  // Print empty line for better CLI output.
  console.log();
}
