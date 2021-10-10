import fs from "fs";

const input = fs.readFileSync("/dev/stdin", "utf8");

let N = input.split("\n")[0];
for (const _ of [...Array(4 - N.length)]) {
  N = "0" + N;
}

console.log(N);
