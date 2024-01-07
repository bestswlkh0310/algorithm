import java.lang.StringBuilder

fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()
    val inp = readln().toInt()

    val sb = StringBuilder()
    for (i in 0 until inp) {
        val (a, b) = br.readLine().split(" ").map { it.toInt() }
        sb.append((a + b).toString() + "\n")
    }
    print(sb)

    bw.close()
}