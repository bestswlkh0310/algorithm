fun main() {
    val n = readln().toInt()
    val arr = arrayListOf<Int>()
    for (i in 0 until n) {
        readln().split(" ").forEach { arr.add(it.toInt()) }
    }
    println(arr.sorted()[arr.size - n])
}