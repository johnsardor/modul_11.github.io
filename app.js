let tg = window.Telegram.WebApp;
tg.expand();

tg.MainButton.textColor = "#FFFFFF"
tg.MainButton.color = "#2cab37"

let btn1 = document.getElementById("btn1")
let btn2 = document.getElementById("btn2")
let btn3 = document.getElementById("btn3")
let btn4 = document.getElementById("btn4")
let item = ""


btn1.addEventListener("click",function () {
    tg.MainButton.setText("bnt1 bosildi")
    item = "Nomi :Burger" +
        "Narxi : 3$";
    tg.MainButton.show();
});
btn2.addEventListener("click",function () {
    tg.MainButton.setText("bnt2 bosildi")
    item = "Nomi: Pepsi" +
        "Narxi: 1$";

    tg.MainButton.show();
});
btn3.addEventListener("click",function () {
    tg.MainButton.setText("bnt3 bosildi")
    item = "Nomi: Cola" +
        "Narxi: 1$";
    tg.MainButton.show();
});
btn4.addEventListener("click",function () {
    tg.MainButton.setText("bnt4 bosildi")
    item = "Nomi: KFC" +
        "Narxi: 6$";
    tg.MainButton.show();
});


Telegram.WebApp.onEvent("mainButtonClicked",function (){
    tg.sendData(item)


});







