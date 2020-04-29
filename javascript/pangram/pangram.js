export const isPangram = (phrase) =>
  new Set(
    phrase
      .toLowerCase()
      .match(/[a-z]/gi)).size == 26;
