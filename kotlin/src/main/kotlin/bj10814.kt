fun main() {

    val n = readln().toInt()
    var arr: MutableList<Pair<Int, String>> = arrayListOf()
    for (i in 0 until n) {
        val (age, str) = readln().split(" ")
        arr.add(Pair(age.toInt(), str))
    }

    var ss = arr.sortedWith(compareBy { it.first })
    ss.forEach { println("${it.first} ${it.second}") }
}