import java.lang.StringBuilder

/*fun main() {
    val n = readln().toInt()
    val arr = readln().split(" ").map { it.toInt() }

}*/

fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()
    val sb = StringBuilder()
    val n = br.readLine().toInt()
    val arr = br.readLine().split(" ").map { it.toInt() }
    val arr1 = arr.distinct().sorted()
//    arr.forEach { print("${arr1.indexOf(it)} ") }
    arr.forEach { sb.append("${arr1.indexOf(it)} ") }
    bw.write("$sb")
    bw.flush()
    bw.close()
}
