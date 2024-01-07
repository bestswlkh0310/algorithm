import java.lang.Long.max

fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()
    val (a, b) = br.readLine().split(" ").map { it.toLong() }
    println(a * b / gcd(a, b))
}

private fun gcd(a: Long, b: Long): Long = if (b != 0L) gcd(b, a % b) else a