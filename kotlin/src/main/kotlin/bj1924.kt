fun main() {
    val (m, d) = readln().split(" ").map { it.toInt() }
    val month = arrayListOf(0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    var sum = 0
    for (i in 0 until m) {
        sum += month[i]
    }
    sum += d

    println(when (sum % 7) {
        0 -> "SUN"
        1 -> "MON"
        2 -> "TUE"
        3 -> "WED"
        4 -> "THU"
        5 -> "FRI"
        6 -> "SAT"
        else -> {}
    })
}