fun main() {
    var arr = Array (100) { Array (100) { false } }

    val n = readln().toInt()
    for (i in 0 until n) {
        val (x, y) = readln().split(" ").map { it.toInt() }

        for (i in y until y + 10) {
            for (j in x until x + 10) {
                arr[i][j] = true
            }
        }
    }
    var sum = 0
    for (i in 0 until 100) {
        for (j in 0 until 100) {
            if (arr[i][j]) sum++
        }
    }
    println(sum)
}