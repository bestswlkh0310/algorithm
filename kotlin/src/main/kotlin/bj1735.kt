import java.lang.Integer.*

fun main() {
    var (a11, b11) = readln().split(" ").map { it.toInt() }
    var (a22, b22) = readln().split(" ").map { it.toInt() }
    var a1 = a11 / gcd(a11, b11)
    var b1 = b11 / gcd(a11, b11)
    var a2 = a22 / gcd(a22, b22)
    var b2 = b22 / gcd(a22, b22)

    //println("$a1 $b1 $a2 $b2")
    val min = min(b1, b2)
    var a: Int = 0
    for (i in min .. b1 * b2) {
        if (i % b1 == 0 && i % b2 == 0) {
            a1 *= i / b1
            a2 *= i / b2
            a = i
            break
        }
        a = b1 * b2
    }

    var aa = a1 + a2
    val aa11 = aa / gcd(aa, a)
    val a111 = a / gcd(aa, a)

    println("$aa11 $a111")
}
private fun gcd(a: Int, b:Int): Int {
    if (a == 1 || b == 1) {
        return 1
    }
    if (b != 0) {
        return gcd(b, a % b)
    } else {
        return a
    }
}