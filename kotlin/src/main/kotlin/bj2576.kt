fun main() {
    var sum = 0
    var arr: MutableList<Int> = arrayListOf()
    for (i in 0 until 7) {
        val inp = readln().toInt()
        if (inp % 2 == 1) {
            sum += inp
            arr.add(inp)
        }
    }
    if (arr.size == 0) return println(-1)
    println(sum)
    println(arr.min())
}