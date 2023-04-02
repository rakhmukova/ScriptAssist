fun factorial(number: Int): Int = if (number == 0) 1 else number * factorial(number - 1)

val number = 5
val result = factorial(number)
println("The factorial of $number is $result")