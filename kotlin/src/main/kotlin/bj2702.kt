import java.lang.Integer.min

fun main() {
    val n = readln().toInt()

    for (i in 0 until n) {
        val (a, b) = readln().split(" ").map { it.toInt() }
        var s: Int = 0
        for (j in min(a, b) .. a * b) {
            if (j % a == 0 && j % b == 0) {
                s = j
                break
            }
        }
        println("$s ${gcd(a, b)}")
    }
}

private fun gcd(a:Int, b:Int): Int = if(b != 0) gcd(b, a % b) else a
