fun main() {
    val n = readln().toInt()

    if (n in 90..100) println("A")
    else if (n in 80..89) println("B")
    else if (n in 70..79) println("C")
    else if (n in 60..69) println("D")
    else println("F")
}