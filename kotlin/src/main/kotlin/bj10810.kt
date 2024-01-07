fun main() {
    var (n, m) = readln().split(" ").map { it.toInt() }

    var arr = Array(n) { 0 }
    for (i in 0 until m) {
        val (a, b, w) = readln().split(" ").map { it.toInt() }
        for (j in a - 1 until b) {
            arr[j] = w
        }
    }
    for (i in 0 until n) {
        print("${arr[i]} ")
    }
}


/*
3 3 0 0 0
3 3 4 4 0
1 1 1 1 0
1 2 1 1 0
 */