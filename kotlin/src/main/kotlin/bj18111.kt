fun main() {
    val br = System.`in`.bufferedReader()
    var (y, x, b) = br.readLine().split(" ").map { it.toLong() }
    val map = Array (y.toInt()) {Array (x.toInt()) {0L} }
    for (i in 0 until y) {
        val a = br.readLine().split(" ").map { it.toLong() }
        for ((j, kj) in a.withIndex()) map[i.toInt()][j] = kj
    }
    var minTime = Long.MAX_VALUE
    var h = 0L
    for (i in 0L .. 256L) {
        var inven = b
        var t = 0L
        for (y1 in 0 until y.toInt()) {
            for (x1 in 0 until x.toInt()) {
                val pos = map[y1][x1]
                if (pos > i) t -= (i - pos) * 2L
                else t += i - pos
                inven += pos - i
            }
        }
        if (inven >= 0 && t in 0..minTime) {
            minTime = t
            h = i
        }
    }
    println("$minTime $h")
}