fun main() {

    val (n, m) = readln().split(" ").map { it.toInt() }
    var arr = Array(n) { it + 1 }

    for (i in 0 until m) {
        val (a, b) = readln().split(" ").map { it.toInt() }

        for (j in 0 .. (b - a) / 2) {
            arr[a + j - 1] = arr[b - j - 1].also { arr[b - j - 1] = arr[a + j - 1] }
        }
    }

    for (i in 0 until n) {
        print("${arr[i]} ")
    }
}
/*
1 2 3 4 5
2 1 3 4 5
2 1 4 3 5
3 4 1 2 5

1 2 3 4 5 6
2 1 3 4 5 6
2 1 5 4 3 6
4 5 1 2 3 6

 */