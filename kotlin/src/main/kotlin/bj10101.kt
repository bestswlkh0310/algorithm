fun main() {
    val a = readln().toInt()
    val b = readln().toInt()
    val c = readln().toInt()

    if (a == 60 && b == 60 && c == 60) println("Equilateral")
    else if (a + b + c == 180 && (a == b || b == c || c == a)) println("Isosceles")
    else if (a + b + c == 180) println("Scalene")
    else println("Error")
}