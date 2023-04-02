open class Person(val name: String, var age: Int) {
    fun printInfo() {
        println("Name: $name, Age: $age")
    }
}

class Student(name: String, age: Int, var grade: Int) : Person(name, age) {
    fun printGrade() {
        println("Grade: $grade")
    }
}

val student = Student("Mary", 18, 12)
student.printInfo()
student.printGrade()