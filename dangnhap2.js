var signin = prompt("nhập vào tên đăng nhập của bạn: ");
var email = prompt("nhập vào email của bạn");
var password = prompt("nhập vào mật khẩu của bạn (Trên 7 chữ cái!!!)");
var password2 = prompt("nhập lại mật khảu của bạn (Nhớ nhập đúng dòng trên nhé!!!) ");

if ((password.length >= 7) && (password === password2)) {
    if (email.includes("@gmail.com")){
        console.log("Tên đăng nhập: ",signin_name);
        console.log("Mật khẩu: ",password);
        console.log("Email: ",email);

    }
    else {
        console.log("Sai địa chỉ gmail.");
        console.log("Nhập lại đê");
        
    }  
}

else {
    console.log("Sai mật khẩu");
    console.log("Nhập lại đê!!!");
}