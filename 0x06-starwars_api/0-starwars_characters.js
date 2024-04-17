#!/usr/bin/node

// Import necessary modules
const request = require('request');

// Function to fetch characters of a movie by ID
function getCharacters(movieId) {
    const url = `https://swapi.dev/api/films/${movieId}/`;
    request(url, function (error, response, body) {
        if (error) {
            console.error('Error:', error);
        } else if (response.statusCode !== 200) {
            console.error('Status:', response.statusCode);
        } else {
            const film = JSON.parse(body);
            film.characters.forEach(characterUrl => {
                request(characterUrl, function (error, response, body) {
                    if (!error && response.statusCode === 200) {
                        const character = JSON.parse(body);
                        console.log(character.name);
                    }
                });
            });
        }
    });
}

// Extract movie ID from command line argument
const movieId = process.argv[2];

// Check if movieId is provided
if (!movieId) {
    console.error('Please provide the Movie ID as a command line argument.');
    process.exit(1);
}

// Call the function to fetch characters
getCharacters(movieId);

