/**
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
 */

function XO(str) {
  arr = str.split("");
  count = {
    count_x: 0,
    count_o: 0,
  };
  for (i in arr) {
    tmp = arr[i].toLowerCase();
    if (tmp == "x") count['count_x'] += 1;

    if (tmp == "o") count['count_o'] += 1;
  }

  return count['count_x'] === count['count_o'];
}

console.log(XO("ooxXmO"));
