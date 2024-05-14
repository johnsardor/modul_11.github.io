
let tg = window.Telegram.WebApp;
tg.expand();

tg.MainButton.textColor = "#FFFFFF"
tg.MainButton.color = "#FC3005"

let rbtn1 = document.getElementById("rbtn1");
let abtn1 = document.getElementById("abtn1");

let rbtn2 = document.getElementById("rbtn2");
let abtn2 = document.getElementById("abtn2");

let rbtn3 = document.getElementById("rbtn3");
let abtn3 = document.getElementById("abtn3");

let rbtn4 = document.getElementById("rbtn4");
let abtn4 = document.getElementById("abtn4");

let item = " "
let num_count = 0

number = document.getElementById("count");

abtn1.addEventListener("click", function () {

    number.innerText = num_count += 1;
    number.style.display = "inner-block";
})
rbtn1.addEventListener("click",function (){
    number.innerText = num_count -= 1;
    number.style.display = "inline-block";
})

count2 = document.getElementById("count2");

abtn2.addEventListener("click", function () {
    count2.innerText = n_count1 += 1;
    count2.style.display = "inline-block";
    tg.MainButton.setText("KFC");
    tg.MainButton.show();
    item = "KfC/10/"+count2.innerText;

})
rbtn2.addEventListener("click", function () {
    count2.innerText = n_count2 -= 1;
    count2.style.display = "inline-block";
    item = "KFC/10/"+count2;
})

count3 = document.getElementById("count3");

abtn3.addEventListener("click", function () {
    count3.innerText = n_count3 += 1;
    count3.style.display = "inline-block";
    tg.MainButton.setText("Pepsi");
    tg.MainButton.show();
    item = "Pepsi/4/"+count1.innerText;

})
rbtn3.addEventListener("click", function () {
    count3.innerText = n_count3 -= 1;
    count3.style.display = "inline-block";
    item = "Pepsi/4/"+count3;
})

count4 = document.getElementById("count4");

abtn4.addEventListener("click", function () {
    count1.innerText = n_count4 += 1;
    count1.style.display = "inline-block";
    tg.MainButton.setText("Cola");
    tg.MainButton.show();
    item = "Cola/5/"+count4.innerText;

})
rbtn4.addEventListener("click", function () {
    count4.innerText = n_count4 -= 1;
    count4.style.display = "inline-block";
    item = "Cola/5/"+count4;
})


// abtn1.addEventListener("click", function () {
//     tg.MainButton.setText("Burger " + num);
//     item = "Burger/3$";
//     tg.MainButton.show();
// });
// rbtn2.addEventListener("click", function () {
//     tg.MainButton.setText("KFC");
//     item = "KFC/10$";
//     tg.MainButton.show();
// });
// abtn3.addEventListener("click", function () {
//     tg.MainButton.setText("LAVASH");
//     item = "LAVASH/4$";
//     tg.MainButton.show();
// });
// rbtn4.addEventListener("click", function () {
//     tg.MainButton.setText("Pizza");
//     item = "Pizza/5$";
//
//     tg.MainButton.show();
// });

Telegram.WebApp.onEvent("mainButtonClicked", function () {
    tg.sendData(item);
});
