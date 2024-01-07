import java.lang.StringBuilder

fun main() {
    var sb = StringBuilder()
    val bw = System.out.bufferedWriter()
    var arr = ArrayDeque<Int>()
    val n = readln().toInt()

    for (i in 0 until n) {
        val str = readln().split(" ")
        try {
            if (str[0] == "push_front") arr.add(0, str[1].toInt())
            else if (str[0] == "push_back") arr.add(str[1].toInt())
            else if (str[0] == "pop_front") { sb.append("${arr[0]}\n"); arr.removeFirst() }
            else if (str[0] == "pop_back") { sb.append("${arr.last()}\n"); arr.removeLast() }
            else if (str[0] == "size") { sb.append("${arr.size}\n") }
            else if (str[0] == "empty") { if (arr.size == 0) sb.append("1\n") else sb.append("0\n") }
            else if (str[0] == "front") { sb.append("${arr[0]}\n") }
            else if (str[0] == "back") { sb.append("${arr.last()}\n") }
        } catch (e: Exception) {
            sb.append("-1\n")
        }
    }
    bw.write("$sb")
    bw.flush()
    bw.close()
}