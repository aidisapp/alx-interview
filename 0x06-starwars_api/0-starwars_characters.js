#!/usr/bin/node

import request from 'request';

// Get the movie ID from command line arguments
const movieId = process.argv[2];

// Make a request to the /films/ endpoint using the provided movie ID
request(`https://swapi.dev/api/films/${movieId}/`, (err, _res, body) => {
  if (err) throw err;

  // Parse the response body to get character URLs
  const characters = JSON.parse(body).characters;

  // Call the function to print character names in order
  printCharacterNames(characters, 0);
});

// Function to print character names recursively
const printCharacterNames = (characters, index) => {
  if (index === characters.length) return; // Stop condition

  // Request each character's data
  request(characters[index], function (err, _res, body) {
          if (err) throw err;

          // Print the character name
          console.log(JSON.parse(body).name);

          // Recursive call to process the next character
          printCharacterNames(characters, index + 1);
      });
};
