import java.math.BigInteger

fun main() {
    var (a, b) = readln().split(" ").map { it.toBigInteger() }
    var sum = BigInteger.ONE
    for (i in 1 .. a.toInt()) {
        sum = sum * BigInteger("$i") % b
    }
    println(sum)
}