var queue = [];
queue.push(2);         // queue is now [2]
queue.push(5);         // queue is now [2, 5]

if(queue.length != 1){
    queue.shift(); // queue is now [5]
}
queue.push(7);         // queue is now [2, 5]


switch(queue.length){
    case 0:
        console.log(0)
    case 1:
        console.log(1)
    case 2:
        console.log(2)
}