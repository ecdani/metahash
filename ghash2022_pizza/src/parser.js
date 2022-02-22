const fs = require('fs');

exports.parse = filename => {
  console.log(`- Parsing "${filename}" -`);

  const content = fs.readFileSync(`input/${filename}`, 'UTF-8');
  const lines = content.split(/\n/);

  const total_clients = lines.shift();
  let clients = [];

  for (let i = 0; i < total_clients; i++) {
    clients[i] = {
      total_ingredients_liked: 0,
      ingredients_liked: [],
      total_ingredients_disliked: 0,
      ingredients_disliked: [],
    };

    let ingredients_liked_line = lines.shift().split(' ');
    clients[i].total_ingredients_liked = ingredients_liked_line.shift();
    clients[i].ingredients_liked = ingredients_liked_line;

    let ingredients_disliked_line = lines.shift().split(' ');
    clients[i].total_ingredients_disliked = ingredients_disliked_line.shift();
    clients[i].ingredients_disliked = ingredients_disliked_line;
  }

  return {total_clients, clients};
}
