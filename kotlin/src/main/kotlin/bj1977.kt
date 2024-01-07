import java.lang.Math.pow
import kotlin.math.*

fun main() {
    val s = readln().toInt()
    val l = readln().toInt()
    var sum = 0

    for (i in ceil(s.toDouble()).toInt() .. floor(l.toDouble()).toInt()) {
        if ((sqrt(i.toDouble()) % 1) == 0.0) {
            sum += i
        }
    }
    if (sum > 0) {
        println(sum)
        println(pow(ceil(sqrt(s.toDouble())), 2.0).toInt())
    } else {
        println(-1)
    }
}