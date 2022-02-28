const fs = require('fs');
const Contributor = require("./Contributor");
const Project = require("./Project");

exports.parse = filename => {
  console.log(`- Parsing "${filename}" -`);

  const content = fs.readFileSync(`input/${filename}`, 'UTF-8');
  const lines = content.split(/\n/);

  // First line, number of contributors and nº of projects
  const [totalContributors, totalProjects] = lines.shift().split(" ");

  const contributors = [];
  const projects = [];
  for (let i = 0; i < totalContributors; i++) {
    const [name, totalSkills] = lines.shift().split(" ");
    const c = new Contributor({ name, totalSkills});

    for (let j = 0; j < totalSkills; j++) {
      const [skillName, level] = lines.shift().split(" ");

      c.addSkill({ name: skillName, level: parseInt(level)})
    }
    contributors.push(c);
  }

  let highestDeadline = 0;
  for (let i = 0; i < totalProjects; i++) {
    const [name, days, score, deadline, roles] = lines.shift().split(" ");
    const p = new Project({name, days, score, deadline, roles});

    // console.log(deadline);
    if (parseInt(deadline) > parseInt(highestDeadline)) {
      highestDeadline = parseInt(deadline);
    }

    for (let j = 0; j < roles; j++) {
      const [skillName, level] = lines.shift().split(" ");
      p.addSkillNedded({name: skillName, level: parseInt(level)});
    }
    projects.push(p);
  }

  return {totalContributors, totalProjects, highestDeadline, contributors, projects};
}
