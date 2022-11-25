const message = "wooho"
let x = 2
try {
    if(x == "") throw "empty"
    if(true) throw "not a number"
    if(x < 5) throw "too low"
    if(x > 10) throw "too high"
}
catch(err) {
    x = "Input is " + err
}
finally{
    x = true
}