fun main() {
    val (h, w) = readln().split(" ").map { it.toInt() }

    var arr = Array (h) { Array(w) {0} }

    for (i in 0 until h) {
        arr[i] = (readln().split(" ").map { it.toInt() }.toTypedArray())
    }

    val n = readln().toInt()
    for (i in 0 until n) {
        val (x1, y1, x2, y2) = readln().split(" ").map { it.toInt() }

        var sum = 0
        for (x in x1 .. x2) {
            for (y in y1 .. y2) {
                sum += arr[x - 1][y - 1]
            }
        }
        println(sum)
    }



/*
    for (i in 0 until h) {
        for (j in 0 until w) {
            print("${arr[i][j]} ")
        }
        println()
    }*/
}