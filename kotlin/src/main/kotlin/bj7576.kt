import kotlin.math.min

fun main() {
    val (x, y) = readln().split(" ").map { it.toInt() }

    for (i in 0 until y) {
        arr.add(readln().split(" ").map { it.toInt() }.toMutableList())
    }

    var tmArr = Array(y){Array(x){1}.toMutableList() }.toMutableList()
    dis = tmArr

    go(3, 5, 0)

    arr.forEach { if (it.contains(0)) { return println(-1) } }

    show(dis, y, x)
    println(sum)
}

private var arr: MutableList<MutableList<Int>> = arrayListOf()
private var dis: MutableList<MutableList<Int>> = arrayListOf()
private var sum = Int.MAX_VALUE

private fun go(y: Int, x: Int, day: Int) {
    try {
        if (arr[y + 1][x] == 0) {
            arr[y + 1][x] = 1
            dis[y + 1][x]++
            arr.forEach { if (!it.contains(0)) sum = min(day, sum) }
            go(y + 1, x, day + 1)
        }
    } catch (e: Exception) {}
    try {
        if (arr[y - 1][x] == 0) {
            arr[y - 1][x] = 1
            dis[y - 1][x]++

            arr.forEach { if (!it.contains(0)) sum = min(day, sum) }
            go(y - 1, x, day + 1)
        }
    } catch (e: Exception) {}
    try {
        if (arr[y][x + 1] == 0) {
            arr[y][x + 1] = 1
            dis[y][x + 1]++

            arr.forEach { if (!it.contains(0)) sum = min(day, sum) }
            go(y, x + 1, day + 1)
        }
    } catch (e: Exception) {}
    try {
        if (arr[y][x - 1] == 0) {
            arr[y][x - 1] = 1
            dis[y][x - 1]++

            arr.forEach { if (!it.contains(0)) sum = min(day, sum) }
            go(y, x - 1, day + 1)
        }
    } catch (e: Exception) {}

    show(arr, 4, 6)
}

private fun show(arr: MutableList<MutableList<Int>>, y: Int, x: Int) {
    for (i in 0 until y) {
        for (j in 0 until x) {
            print("${arr[i][j]} ")
        }
        println()
    }
    println()
}