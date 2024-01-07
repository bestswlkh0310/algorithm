fun main() {
    val inp = readln().toInt()
    var arr = Array (inp) { Array (inp) { " " } }
    for (i in 0 until inp) {
        arr[i][0] = "*"
        arr[0][i] = "*"
        arr[i][inp - 1] = "*"
        arr[inp - 1][i] = "*"
        arr[i][i] = "*"
        arr[i][inp - i - 1] = "*"
    }
    for (i in 0 until inp) {
        for (j in 0 until inp) {
            print(arr[i][j])
        }
        println()
    }
}