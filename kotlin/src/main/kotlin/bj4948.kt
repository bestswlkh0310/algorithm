import kotlin.math.sqrt

fun main() {
    while (true) {
        val n = readln().toInt()
        if (n == 0) break
        var sum = 0

        loop@
        for (i in n + 1 .. n * 2) {
            for (j in 2 .. sqrt(i.toDouble()).toInt()) {
                if (i % j == 0)
                    continue@loop
            }
            sum++
        }
        println(sum)
    }
}