fun main() {
    var arr: MutableList<MutableList<Int>> = Array(3) { Array (2) { 0 }.toMutableList() }.toMutableList()
    for (i in 0 until 3) {
        val (a, b) = readln().split(" ").map { it.toInt() }
        arr[i][0] = a
        arr[i][1] = b
    }
    for (i in 0 until 3) {
        for (j in 0 until 3) {
            if (arr[j][0] == arr[i][0] && i != j) {
                arr[j][0] = 0
                arr[i][0] = 0
            }
            if (arr[j][1] == arr[i][1] && i != j) {
                arr[j][1] = 0
                arr[i][1] = 0
            }
        }
    }
    for (i in 0 until 3) {
        if (arr[i][0] != 0) print("${arr[i][0]} ")
    }
    for (i in 0 until 3) {
        if (arr[i][1] != 0) println(arr[i][1])
    }
}