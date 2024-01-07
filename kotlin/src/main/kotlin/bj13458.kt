import kotlin.math.ceil

fun main() {
    val n = readln().toLong()
    val inp: MutableList<Long> = readln().split(" ").map { it.toLong() }.toMutableList()
    var arr: MutableList<Long> = arrayListOf()
    val (a, b) = readln().split(" ").map { it.toLong() }
    for (i in 0 until n) {
        inp[i.toInt()] -= a
        if (inp[i.toInt()] > 0) {
            arr.add(ceil(inp[i.toInt()] / b.toDouble()).toLong())
        }
    }
    println(arr.sum() + n)
}