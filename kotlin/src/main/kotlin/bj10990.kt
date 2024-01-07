fun main() {
    val n = readln().toInt()
    repeat(n - 1) { print(" ")}
    println("*")
    for (i in 0 until n - 1) {
        for (j in i until n - 2)
            print(" ")
        print("*")
        for (j in 0 .. i * 2)
            print(" ")
        println("*")
    }
}