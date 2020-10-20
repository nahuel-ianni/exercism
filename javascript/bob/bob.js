export const hey = (message) => {
  const phrase = message.trim();
  const phraseWasShouted = isYelling(phrase) && containsChar(message);
  let response = "Whatever.";

  if (isSilent(phrase))
    response = "Fine. Be that way!";

  else if (isQuestion(phrase))
    response = phraseWasShouted
      ? "Calm down, I know what I'm doing!"
      : "Sure.";

  else if (phraseWasShouted)
    response = "Whoa, chill out!";

  return response;
};

const containsChar = (message) =>
  [...message.toLowerCase()].some(c => c.match(/[a-z]/i));

const isQuestion = (message) => message.endsWith("?");

const isSilent = (message) => !message;

const isYelling = (message) => message === message.toUpperCase();