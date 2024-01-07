fun main() {
    val m = readln().toInt()
    val n = readln().toInt()
    var sum = 0
    var arr: MutableList<Int> = arrayListOf()
    loop@
    for (i in m .. n) {
        for (j in 2 until i) {
            if (i % j == 0) {
                continue@loop
            }
        }
        if (i == 1) continue@loop
        arr.add(i)
        sum += i
    }
    try {
        arr[0]
    } catch (e: Exception) {
        return println(-1)}
    println(sum)
    if (arr[0] == 2) println(2)
    else println(arr[0])
}