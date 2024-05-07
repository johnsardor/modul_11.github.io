let tg = window.Telegram.WebApp;
tg.expand();

tg.MainButton.textColor = "#FFFFFF"
tg.MainButton.color = "#2cab37"

let btn1 = document.getElementById("btn1")
let btn2 = document.getElementById("btn2")
let btn3 = document.getElementById("btn3")
let btn4 = document.getElementById("btn4")
let btn5 = document.getElementById("btn5")

btn1.addEventListener("Click",function () {
    tg.MainButton.setText("bnt1 bosildi")
    tg.MainButton.show();
})
btn2.addEventListener("Click",function () {
    tg.MainButton.setText("bnt2 bosildi")
    tg.MainButton.show();
})
btn3.addEventListener("Click",function () {
    tg.MainButton.setText("bnt3 bosildi")
    tg.MainButton.show();
})
btn4.addEventListener("Click",function () {
    tg.MainButton.setText("bnt4 bosildi")
    tg.MainButton.show();
})
btn5.addEventListener("Click",function () {
    tg.MainButton.setText("bnt5 bosildi")
    tg.MainButton.show();
})

