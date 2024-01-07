fun main() {
    val num = readln().toLong()
    for (j in 0L until num) {
        var arr = arrayListOf(1L, 1L, 1L, 2L, 2L, 3L, 4L, 5L, 7L, 9L)
        val n = readln().toLong()
        for (i in arr.size - 1..n) {
            arr.add(arr[i.toInt()] + arr[i.toInt() - 4])
        }
        println(arr[n.toInt() - 1])
    }
}