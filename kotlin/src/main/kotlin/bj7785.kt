import java.lang.StringBuilder

fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()
    val sb = StringBuilder()
    val n = br.readLine().toInt()
    var arr = arrayListOf<String>()

    for (i in 0 until n) {
        val (str, mode) = br.readLine().split(" ")
        if (mode[0] == 'e') {
            arr.add(str)
        } else {
            arr.remove(str)
        }
    }
    arr.sort()
    arr.reverse()

    for (i in arr) {
        sb.append("$i\n")
    }
    bw.write("$sb")
    bw.flush()
    bw.close()
}