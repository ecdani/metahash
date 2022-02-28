class Project {
    constructor({name, days, score, deadline, roles}) {
        this.name = name;
        this.days = parseInt(days);
        this.score = parseInt(score);
        this.deadline = parseInt(deadline);
        this.roles = parseInt(roles);

        this.skillsNeeded = [];
        this.finished = false;
        this.active = false;
        this.startedOn = 0;
        this.contributorsAssigned = [];
    }

    addSkillNedded(skill) {
        this.skillsNeeded.push(skill);
    }

    calcScore(highestDeadline) {
      return (highestDeadline - this.days) * 0.5 + this.score + this.deadline * 0.8 + this.roles * 0.4
    }

    isUsable() {
      return !this.finished && !this.active
    }

    findContributors = (contributors) => {
      let tempSkills = [];
      this.skillsNeeded

      const proj = this;
      let selectedContributors = [];
      const meh = contributors.filter((contributor) => {
        contributor.skills.forEach(skill => {
          if (tempSkills.find(tempSkill => { tempSkill.name === skill.name })) return false;

          if (proj.skillsNeeded.find(neededSkill => {
            neededSkill.name === skill.name && neededSkill.level <= skill.level
          })) {
            tempSkills.push(skill);
            contributor.free = false;
            proj.contributorsAssigned.push(contributor);
            selectedContributors.push(contributor);
          }
        });
      });

      return selectedContributors;
    };

    amountOfSkillsOfContrib(contributor) {
      let tempSkills = [];
      this.skillsNeeded.forEach(skill => {
          if (contributor.has(skill)) {
            tempSkills.push(skill)
          }

      });
      return tempSkills;
    }

    findContributors2 = (contributors) => {
      let tempSkills = [];
      let viableSkillsOfContrib = [];
      let newviableSkillsOfContrib = [];
      this.skillsNeeded.forEach(skill => {
        contributors.every(contrib => {
          newviableSkillsOfContrib = this.amountOfSkillsOfContrib(contrib);
          if (newviableSkillsOfContrib.length == this.skillsNeeded.length) {
            viableSkillsOfContrib = newviableSkillsOfContrib;

            // break;
          }
          if (newviableSkillsOfContrib.length > viableSkillsOfContrib.length){
            viableSkillsOfContrib = newviableSkillsOfContrib
          }
        })

      });
// skill del proyecto
      // nskills previas = 0
      // contributor (mentor) elegido.
      // Para cada contributor,
       // Para cada skill del proyecto
        // Si el contributor la tiene y tiene level suficiente, +1 var temporal de skills
        // Sino nada

      // Si el número de skills > nskills previas  Lo asigno (nskill previas y contributor)
      // Si el numero de skills == nskills necesarias, me quedo con el mentor.

      // añadimos el mentor a la lista de
      // Para los becarios:
      // ¿Como elegir becarios?
      // para cada skill del mentor (a partir de la primera)
        // Bucle en los trabajadores, con el primer trabajador con un level inferior al requerido.
           // añadimos el trabajador a la lista de contrib


      const proj = this;
      return contributors.filter((contributor) => {
        contributor.skills.forEach(function skill() {
          if (tempSkills.find(tempSkill => { tempSkill === skill.name })) return false;

          if (proj.skillsNeeded.find(neededSkill => { neededSkill === skill.name })) {
            tempSkills.push(skill.name);
            contributor.free = false;
            project.contributorsAssigned.push(contributor);
            return true;
          }
        });
      });
    };

}

module.exports = Project;

/*
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
