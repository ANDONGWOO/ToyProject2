var start;
var end;
var end_time;
function test1() {
    start = new Date().getTime();
}

function test2() {
    end = new Date().getTime();
    end_time = new Date(end-start);
    console.log(end_time.getMinutes())
}

