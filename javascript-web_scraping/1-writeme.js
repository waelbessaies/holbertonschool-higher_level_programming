#!/usr/bin/node
const fs = require('fs');

const content = 'Some content!';

fs.writeFile(process.argv[2], process.argv[3],'utf8', content, err => {
  if (err) {
    console.error(err);
  }
  // fichier écrit avec succès
});
