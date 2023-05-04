var start;
var end;
var end_time;
var start_now;

function test1() {
    start = new Date().getTime();
    // start_now=new Date();
    //start-start_now 화면에서 보여주기
}
function test2() {
    end = new Date();
    end_time = new Date(end-start);
    min = end_time.getMinutes()
    sec = end_time.getSeconds()
    milisec = end_time.getMilliseconds()

    document.getElementById("testM").innerText =min
    document.getElementById("tests").innerText =sec
    document.getElementById("testm").innerText =milisec
}

// function test3(){
//     let count = 0;
//     setInterval(() => console.log(++count), 1000);
// }

// function test4(){
//     let count = 0;
//     setInterval(() => console.log(++count), 1000);
// }
// test3()
//clearInterval(변수) 중단
//일정시간 후 실행 setInterval(() => console.log(++count), 1000);


