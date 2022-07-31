/**
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')   # elloHay orldway !
 */

function pig_it(str) {
  arr = str.split(" ");
  pig = arr.map((t) => {
    if (t.match(/^[0-9a-zA-Z]/)) {
      tmp = t.split("");
      first = tmp[0];
      tmp.splice(0, 1);
      tmp.push(first, "ay");
      return tmp.join("");
    }
    return t;
  });

  return pig.join(" ");
}

console.log(pig_it("Pig latin is cool !!!!! %%%"));
