import java.lang.Exception
import java.lang.StringBuilder

fun main() {
    val sb = StringBuilder()
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()

    var str = br.readLine()
    val boom = br.readLine()

    while (str.contains(boom)) {
        str = str.replace(boom, "")
    }
    if (str == "") return println("FRULA")
    sb.append(str)
    bw.write("$sb")
    bw.flush()
    bw.close()
}