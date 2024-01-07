import java.lang.StringBuilder

fun main() {
    val sb = StringBuilder()
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()

    val a = br.readLine().toInt()
    val inp1 = br.readLine().split(" ").map { it.toLong() }
    val b = br.readLine().toInt()
    val inp2 = br.readLine().split(" ").map { it.toLong() }

    for (i in inp2) {
        if (inp1.contains(i)) sb.append("1 ")
        else sb.append("0 ")
    }

    bw.write("$sb")
    bw.flush()
    bw.close()
}