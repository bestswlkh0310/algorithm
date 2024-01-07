import java.lang.Math.pow

fun main() {
    val n = readln().toInt()
    val str = readln().toCharArray().map { it - 'a' + 1 }
    var sum = 0L

    for ((i, j) in str.withIndex()) {
        sum += j.toLong() * pow(31.0, i.toDouble()).toLong()
    }
//    println(str)
    println(sum)
}