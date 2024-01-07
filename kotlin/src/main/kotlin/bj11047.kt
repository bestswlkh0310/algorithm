fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    var arr = arrayListOf<Int>()
    var sum = 0
    var cnt = 0
    for (i in 0 until n) {
        arr.add(readln().toInt())
    }
    arr.reverse()
    while (m != sum) {
        for (i in arr) {
            if (m - (sum + i) >= 0) {
                sum += i
                cnt++
                break
            }
        }
//        println(sum)
    }
    println(cnt)
}