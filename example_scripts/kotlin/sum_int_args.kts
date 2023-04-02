var sum = 0

for (arg in args) {
    var num = arg.toIntOrNull()

    if (num == null) {
        println("Invalid argument: $arg")
    } else {
        sum += num
    }
}

println("The sum of the arguments is: $sum")