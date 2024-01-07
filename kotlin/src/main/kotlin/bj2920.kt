fun main() {
    val inp = readln().split(" ").map { it.toInt() }

    var stack = 0
    for (i in 1 .. 8)
        if (inp[i - 1] == i) stack++
    if (stack == 8) return println("ascending")
    stack = 0
    for (i in 8 downTo  1)
        if (inp[8 - i] == i) stack++
    if (stack == 8) return println("descending")
    println("mixed")
}