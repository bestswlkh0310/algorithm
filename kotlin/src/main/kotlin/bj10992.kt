fun main() {
    val n = readln().toInt()

    if (n == 1) { print("*"); return }
    repeat(n - 1) { print(" ")}
    println("*")
    for (i in 0 until n - 2) {
        for (j in i until n - 2)
            print(" ")
        print("*")
        for (j in 0 until i)
            print("  ")
        println(" *")
    }
    repeat(n * 2 - 1) { print("*") }
}