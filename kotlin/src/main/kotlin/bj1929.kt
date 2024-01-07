import kotlin.math.sqrt

fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()
    var sb = StringBuilder()
    var (a, b) = br.readLine().split(" ").map { it.toInt() }
    val arr = ArrayDeque(setOf(2))

    if (a % 2 == 0) a--
    if (a <= 2) {
        bw.write("2\n")
        a = 3
    }

    loop@
    for (i in a .. b step 2) {
        val sqrt = sqrt(i.toDouble())
        for (k in arr) {
            if (i % k == 0) continue@loop
            if (k > sqrt) break
        }
        if (!arr.contains(i))
            arr.add(i)
        sb.append("$i\n")
    }
    bw.write("$sb")
    bw.flush()
    bw.close()
}