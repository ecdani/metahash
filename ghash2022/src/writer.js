const fs = require('fs');

exports.write = (filename, plannedProjects) => {
  console.log(`- Writing "${filename}"" -`);

  let content = String(plannedProjects.length + "\n");

  plannedProjects.forEach(plannedProject => {
    content += plannedProject.name + "\n";
    const roleNames = plannedProject.roles.map(role => role.name);
    content += roleNames.join(' ') + "\n";
  });


  fs.writeFile(`output/${filename}`, content, err => {
    if (err) {
      throw err;
    }
  });
}
