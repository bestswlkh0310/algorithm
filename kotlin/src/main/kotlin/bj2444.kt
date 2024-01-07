import kotlin.math.abs

fun main() {
    val lst: MutableList<Int> = (0 until 26).map { 0 }.toMutableList()
    val str = readln().uppercase()
    var best: Int = 0
    for (i in str.indices) {
        lst[str[i].code - 65]++
    }
    var ind = 0
    for ((j, i) in lst.withIndex()) {
        if (best < i) {
            best = i
            ind = j
        }
    }
    var sum = 0
    for (i in 0 until 26) {
        if (best == lst[i]) {
            sum++
        }
        if (sum == 2) {
            return println("?")
        }
    }
    print((ind + 65).toChar())
}