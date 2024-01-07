fun main() {
    val n = readln().toInt()
    var arr = arrayListOf<Int>()

    for (i in 0 until n) {
        val a = readln().toInt()
        if (a == 0) {
            arr.removeLast()
        } else {
            arr.add(a)
        }
    }

    println(arr.sum())
}