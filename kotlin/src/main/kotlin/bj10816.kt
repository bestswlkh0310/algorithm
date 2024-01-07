import java.lang.StringBuilder

fun main() {
    var sb = StringBuilder()
    val bw = System.out.bufferedWriter()
    var arr: MutableList<Int> = MutableList(21000000) { 0 }
    val a = readln().toInt()
    readln().split(" ").map { it.toInt() }.forEach { arr[it + 10500000]++ }
    val b = readln().toInt()
    val arr2 = readln().split(" ").map { it.toInt() }

    arr2.forEach { sb.append("${arr[it + 10500000]} ") }
    bw.write("$sb")
    bw.flush()
    bw.close()

}