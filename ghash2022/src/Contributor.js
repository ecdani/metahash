class Contributor {
  constructor({ name, totalSkills, skills }) {
    this.name = name;
    this.totalSkills = parseInt(totalSkills);
    this.freeOnDay = 0;
    this.skills = [];
    this.free = true;
  }

  addSkill(skill) {
    this.skills.push(skill);
  }

  setFreeOnDay(day) {
      this.freeOnDay = day;
  }
}

module.exports = Contributor;

/* {
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
  } */
