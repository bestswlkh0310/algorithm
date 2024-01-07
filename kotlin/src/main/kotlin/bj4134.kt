import kotlin.math.sqrt

fun main() {
    val n = readln().toInt()
    for (i in 0 until n) {
        val inp = readln().toLong()

        if (inp <= 2) {
            println(2)
            continue
        }
        loop@
        for (j in inp .. inp * 2) {
            for (k in 2 .. (sqrt(inp.toDouble()) + 1).toInt()) {
                if (j % k == 0L) continue@loop
            }
            println(j)
            break
        }
    }
}