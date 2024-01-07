fun main() {
    val n = readln().toInt()
    var arr = Array (n) { Array(2) { 0 } }
    for (i in 0 until n) {
        val (a, b) = readln().split(" ").map { it.toInt() }
        arr[i][0] = a
        arr[i][1] = b
    }
    var arr2 = Array (n) { 1 }
    for (i in 0 until n) {
        for (j in 0 until n) {
            if (i == j) continue
            if (arr[i][0] < arr[j][0] && arr[i][1] < arr[j][1]) arr2[i]++
        }
    }

    for (i in 0 until n) {
        print("${arr2[i]} ")
    }
}