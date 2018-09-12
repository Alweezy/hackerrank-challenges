function processData(input) {
    //Enter your code here
    const data = input.split('\n');
    let myHeap = [];
    const numberOfqueries = data.shift();
    for (let i = 0; i < numberOfqueries; i++) {
        const option = parseInt(data[i])
        let item = parseInt(data[i].substr(2));

        if (option == 1) {
            myHeap.push(item);
        } else if (option == 2) {
            index = myHeap.indexOf(item)
            myHeap.splice(index, 1);
        } else {
            let minimum = Infinity;
            for (let j = 0; j < myHeap.length; j++){
                if (myHeap[j] < minimum) {
                    minimum = myHeap[j];
                }
            }
            console.log(minimum);
        }
    }
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
    processData(_input);
});
