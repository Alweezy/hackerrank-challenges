'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the icecreamParlor function below.
function icecreamParlor(m, icecreamFlavours) {
    for(let i = 0, len = icecreamFlavours.length; i < len - 1;  i++){
        for (let j = i + 1;  j < len; j++ ) {
            if (icecreamFlavours[i] + icecreamFlavours[j] === m) {
                return [i + 1, j + 1];
            }
        }
    }

}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const t = parseInt(readLine(), 10);

    for (let tItr = 0; tItr < t; tItr++) {
        const m = parseInt(readLine(), 10);

        const n = parseInt(readLine(), 10);

        const icecreamFlavours = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));

        let result = icecreamParlor(m, icecreamFlavours);

        ws.write(result.join(" ") + "\n");
    }

    ws.end();
}
