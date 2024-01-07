import java.lang.Math.sqrt

fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()
    val (a, b) = br.readLine().split(" ").map { it.toInt() }

    val isPrime = BooleanArray(b + 1) { true }
    val primes = mutableListOf<Int>()

    for (i in 2..sqrt(b.toDouble()).toInt()) {
        if (isPrime[i]) {
            for (j in i * i..b step i) {
                isPrime[j] = false
            }
        }
    }

    for (i in maxOf(2, a) .. b) {
        if (isPrime[i]) {
            primes.add(i)
        }
    }

    with(bw) {
        for (prime in primes) {
            println(prime)
        }
        flush()
        close()
    }
}