fun main() {
    val n = readln().toInt()
    val k = readln().toInt()
    val arr = arrayListOf<Int>()
    for (i in 1 until n) {
        for (j in i - 1 downTo 2) {
            if (i % j == 0) {
                arr.add(j)
                println("$i $j")
                break
            }
        }
    }
    println(arr.count { it <= k })
}