/**\
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
 */

function humanReadable(seconds) {
  var hrs = parseInt(seconds / 3600);
  var min = parseInt((seconds / 60) % 60);
  var sec = seconds % 60;

  function format(x) {
    return x > 9 ? x : `0${x}`;
  }

  return `${format(hrs)}:${format(min)}:${format(sec)}`;
}

console.log(humanReadable(359999));
console.log(humanReadable(1000));
console.log(humanReadable(10000));
console.log(humanReadable(0));
