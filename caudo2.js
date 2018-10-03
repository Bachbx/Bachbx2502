console.log("Con nhện có mấy chân");
console.log("1. 10 chân");
console.log("2. 4 chân");
console.log("3. 6 chân");
console.log("4. Không có chân nào");

var answer = prompt("Câu trả lời của bạn:");

if (answer === "1"){
    console.log("Bạn nên đi viện tâm thần!!!");
}

else if (answer === "2"){
    console.log("Đúng rồi bạn ơi!!!");
}

else if (answer ==="3"){
    console.log("Sai rồi bạn ơi!!!");

}

else if (answer === "4"){
    console.log("Bạn nên đi khám mắt rồi nhìn lại nhện đi!!!");
}

else{
    console.log("Bạn phải nhập 1, 2, 3, 4");
    console.log("Nhập lại đê!!!");
}