fun main() {
    val n = readln().toInt()

    if (n % 400 == 0 || (n % 100 != 0 && n % 4 == 0)) println(1)
    else println(0)
}