import java.lang.StringBuilder

fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()
    val sb = StringBuilder()

    val (a, b) = br.readLine().split(" ").map { it.toInt() }
    var arr1 = mutableSetOf<String>()
    var arr2 = mutableSetOf<String>()
    repeat(a) {arr1.add(br.readLine())}
    repeat(b) {arr2.add(br.readLine())}

    val arr3 = arr2.intersect(arr1).toMutableList().sorted()

    bw.write("${arr3.size}\n")
    for (i in arr3) { sb.append("$i\n") }
    bw.write("$sb")
    bw.flush()
    bw.close()
}