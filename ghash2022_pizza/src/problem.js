const parser = require('./parser.js');
const writer = require('./writer.js');

exports.resolve = filename => {
  const start_time = Date.now();

  const { total_clients, clients } = parser.parse(filename);

  console.log(`- Resolving "${filename}" -`);

  // Braindead solution: make the pizza with ingredients nobody dislikes.
  // Remove clients who dislike more ingredients than they like.
  clients.filter(client => client.total_ingredients_liked > client.total_ingredients_disliked);

  let pizza_ingredients = [];
  clients.forEach(client => {
    // Add liked ingredients.
    client.ingredients_liked.forEach(liked_ingredient => {
      if (pizza_ingredients.find(pizza_ingredient => pizza_ingredient == liked_ingredient)) {
        return;
      }

      pizza_ingredients.push(liked_ingredient);
    });
  });

  clients.forEach(client => {
    // Remove ingredients someone dislikes.
    client.ingredients_disliked.forEach(disliked_ingredient => {
      if (!pizza_ingredients.find(pizza_ingredient => pizza_ingredient == disliked_ingredient)) {
        return;
      }

      pizza_ingredients.splice(pizza_ingredients.indexOf(disliked_ingredient), 1);
    });
  });

  writer.write(filename.replace('.in','.out'), pizza_ingredients);

  const end_time = Date.now();
  console.log(`Processed "${filename}" in ${(end_time - start_time) / 1000} seconds`);

  // Print empty line for better CLI output.
  console.log();
}
