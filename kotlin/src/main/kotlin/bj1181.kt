fun main() {
    val br = System.`in`.bufferedReader()
    println(List(br.readLine().toInt()) {br.readLine()}.toSet()
        .sortedWith(compareBy({it.length}, {it})).joinToString("\n"))
}