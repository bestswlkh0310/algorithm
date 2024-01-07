fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    var arr1:MutableList<MutableList<Int>> = arrayListOf()
    var arr2:MutableList<MutableList<Int>> = arrayListOf()

    for (i in 0 until n) {
        arr1.add(readln().split(" ").map { it.toInt() }.toMutableList() )
    }
    for (i in 0 until n) {
        arr2.add(readln().split(" ").map { it.toInt() }.toMutableList() )
    }
    for (i in 0 until n) {
        for (j in 0 until m) {
            print("${arr1[i][j] + arr2[i][j]} ")
        }
        println()
    }
}