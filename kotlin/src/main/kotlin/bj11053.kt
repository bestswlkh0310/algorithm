fun main() {
    val n = readln().toInt()
    var arr = readln().split(" ").map { it.toInt() }.toMutableList()

    for ((i, n) in arr.withIndex()) {
        if (i == 0) continue
//        println("$i $n")
        if (n < arr[i - 1]) arr[i - 1] = -1
    }

    println(arr.filter { it != -1 }.size)
}