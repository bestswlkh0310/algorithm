fun main() {
    val (a, b) = readln().split(" ").map { it.toInt() }
    var arr = Array (10) { 0L }
    var sum = 0L
    for (i in a..b) {
//        sum += i.toString().sumOf { it-'0' }
        for (j in i.toString()) {
            arr[j.code - '0'.code]++
        }
    }

    arr.forEachIndexed { index, it -> sum += it * index }
    println(sum)
}