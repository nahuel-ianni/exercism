const earthSeconds = 31557600;

const PlanetarySeconds = {
  earth   : earthSeconds,
  mercury : 0.2408467  * earthSeconds,
  venus   : 0.61519726 * earthSeconds,
  mars    : 1.8808158  * earthSeconds,
  jupiter : 11.862615  * earthSeconds,
  saturn  : 29.447498  * earthSeconds,
  uranus  : 84.016846  * earthSeconds,
  neptune : 164.79132  * earthSeconds
}

export const age = (planet, seconds) => 
  Number((seconds / PlanetarySeconds[planet]).toFixed(2));
