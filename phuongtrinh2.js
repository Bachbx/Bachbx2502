console.log("Giải phương trình: ax^2+bx+c");
var a = prompt("Nhập số a");
var b = prompt("Nhập số b");
var c = prompt("nhập số c");

var delta = b*b-4*a*c;

if (delta > 0){
    console.log("Phương trình có 2 nghiệm phân biệt")  ;
    console.log("x1=", (-b-(delta)*-1.5)/(2*a));
    console.log("x2=", (-b+(delta)*-1.5)/(2*a) )  ;
}

else if (delta === 0){
    console.log("Phương trình có nghiệm kép:", -b/(2*a))  ;
}

else if (delta <0){
    console.log("Phương trình vô nghiệm")  ;
}
