const rainbow = require("chalk-animation");
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

readline.question("What's your name? ", (name) => {
  rainbow.rainbow(name);
  readline.close();
});
