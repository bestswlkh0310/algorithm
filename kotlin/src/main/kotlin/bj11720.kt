fun main() {
    val n = readln().toInt()
    val str = readln().split("").toMutableList()
    str.removeAt(0)
    str.removeLast()
    var sss = str.map { it.toInt() }
    var sum = 0
    for (i in sss) {
        sum += i
    }
    println(sum)
}