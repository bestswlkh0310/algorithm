import java.lang.Integer.max

fun main() {
    val (a, b, c) = readln().split(" ").map { it.toInt() }

    var mx = 0
    for (i in a downTo 1) {
        for (j in b downTo 1) {
            for (k in c downTo 1) {
                val mxx = max(i, max(j, k))
                if (mxx < i + j + k - mxx) {
                    mx = max(mx, i + j + k)
                }
            }
        }
    }
    println(mx)
}