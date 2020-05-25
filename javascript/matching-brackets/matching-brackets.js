export const isPaired = (input) => {
  input = input.match(/\[|\]|\(|\)|\{|\}/g)?.join("");

  if (!input) return true;
  
  while (input.includes("()") || input.includes("[]") || input.includes("{}")) {
    input = input.replace("()", "").replace("[]", "").replace("{}", "");
  }

  return input.length == 0;
};
