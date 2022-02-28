const parser = require("./parser.js");
const writer = require("./writer.js");

/*
*  Get proyect without finished or active and order by deadline
*/
// funcion cual es el mejor proyecto
const getBestAvailableProjects = (projects) => {
  const filteredProjects = getFilteredAvailableProjects(projects);

  filteredProjects
    .sort((pA, pB) => pA.deadline - pB.deadline);
}

// p.forEach((project) => {
  // función que traiga los mejores contribuyentes necesarios para ejecutar el proyecto
  // asignar dichos contribuyentes al proyecto y ponerlo como activo <--
// });


/*
*  Get proyect without finished or active and order by deadline
*/
const getFilteredAvailableProjects = (projects) =>
  projects
    .filter(({ finished, active }) => !finished && !active);

/**
 * Ver qué becarios son los mejores
 */
const fillProjectWithContributors = (projects, contributors) => {

}

/*
*  Is available contributors
*/
const areContributorsAvailable = (contributors) => contributors.find((contributor) => contributor.free);

// const findContributors = (project, contributors) => {
//   let tempSkills = [];
//   return contributors.filter(contributor => {
//     contributor.skills.forEach(skill => {
//       if (tempSkills.find(tempSkill => { tempSkill === skill.name })) return false;

//       if (project.skillsNeeded.find(neededSkill => { neededSkill === skill.name })) {
//         tempSkills.push(skill.name);
//         contributor.free = false;
//         return true;
//       }
//     });
//   });
// };

// Terminar proyectos y liberar becarios
const itsANewDay = (day, projects, contributors) => {
  projects.filter(project => {
    if (project.finished || !project.active) {
      return false;
    }
    else {
      return true
    };
  }).forEach(project => {
    if (project.startedOn + day >= project.days) {
      project.finished = true;

      // Liberar becarios
      project.contributorsAssigned.forEach(contributor => {
        contributor.free = true;
      });
    }
  });
};

/**
 * Evaluar como de bueno es el proyecto para pillarlo primero
 */
// const score = (project, contributor, highestDeadline) => {};

/**
 * Asignar los proyectos a los becarios
 */
const assigment = (project, contributor) => {
  const a = project.skillsNeeded.map((skill) => {
    const contributorWithSkill = contributor.filter((c) =>
      c.skills.find((s) => s.name === skill.name)
    );
  });
};

exports.resolve = (filename) => {
  const start_time = Date.now();

  const {
    totalContributors,
    totalProjects,
    highestDeadline,
    contributors,
    projects,
  } = parser.parse(filename);

  console.log(`- Resolving "${filename}" -`);

  let plannedProjects = [];

  // TODO: real solving here...

  // solución meh por días
  for (let day = 0; day < highestDeadline; day++) {
    // comprobar los proyectos que se terminan y liberar a los becarios
    if (day != 0) {
      itsANewDay(day, projects, contributors);
    }

    if (!areContributorsAvailable(contributors)) continue;

    const sortedProjects = projects.sort((projectA, projectB) => {
      projectA.calcScore(highestDeadline) - projectB.calcScore(highestDeadline);
    });

    sortedProjects.forEach(project => {
      if (project.finished || project.active) {
        return;
      }
      const projectContributors = project.findContributors(contributors);
      if (!projectContributors.length || projectContributors.length != project.roles) {
        return;
      }

      project.active = true;
      project.startedOn = day;

      plannedProjects.push({
        'name': project.name,
        'roles': projectContributors,
      });
    });
  }


  writer.write(filename.replace(".in", ".out"), plannedProjects);

  const end_time = Date.now();
  console.log(
    `Processed "${filename}" in ${(end_time - start_time) / 1000} seconds`
  );

  // Print empty line for better CLI output.
  console.log();
};

/*

Datos Random

totalContributors, totalProjects, highestDeadline


Contributors
{
  name: 'Dani',
  totalSkills: 2,
  freeOnDay: 0,
  skills: [
    {
      name: 'C++',
      level: 2,
    },
    {
      name: 'PHP',
      level: 5,
    }
  ]
}

projects
{
  name: "Drupal",
  days: 5,    /// 0.5 ////Duracion (inv)
  score: 20,    ///  1
  deadline: 7,   /// 0.8 (inv)
  roles: 2,       /// 0.4 (inv)
  finished: false, //propia
  active: false, //propia
  skillsNeeded: [
    {
      name: 'PHP',
      level: 2,
    },
    {
      name: 'C++',
      level: 4,
    }
  ]
}
*/

/*
  SOLUTION

  plannedProjects = [
    {
      name: 'Webchat',
      roles: [
        'Fran',
        'Dani',
        'Flopi',
      ],
    },
    ...
  ]
*/
