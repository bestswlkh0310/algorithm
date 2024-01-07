fun main() {
    var arr: MutableList<MutableList<Int>> = arrayListOf(arrayListOf())
    for (i in 0 until 9) {
        arr.add(readln().split(" ").map { it.toInt() }.toMutableList())
    }
    var best = 0
    var x = 0
    var y = 0
    arr.removeAt(0)
    for (i in 0 until 9) {
        for (j in 0 until 9) {
            if (arr[i][j] > best) {
                best = arr[i][j]
                x = i
                y = j
            }
        }
    }
    println(best)
    println("${x + 1} ${y + 1}")
}