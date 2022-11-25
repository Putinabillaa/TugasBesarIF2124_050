const message = "wooho"
let x = 2
try {
    if(x == "") 
        y = "empty"
    else if (x == false){
        y = "empty"
    }
    y = "empty"
}
catch(err) {
    x = "Input is " + err
}
finally{
    x = true
}