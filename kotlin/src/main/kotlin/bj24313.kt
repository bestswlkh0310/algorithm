fun main() {
    val (a, b) = readln().split(" ").map { it.toInt() }
    val c = readln().toInt()
    val n = readln().toInt()

    if (n * (a - c) <= -b) {
        if (a - c > 0) println(0)
        else println(1)
    }
    else {
        println(0)
    }
}

// 7 -2
// 6
// 1