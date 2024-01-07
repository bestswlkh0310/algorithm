fun main() {
    val inp = readln().toInt()
    for (i in 0 until inp) {
        val lst = readln().split(" ").map { it.toInt() }.toMutableList()
        lst.removeAt(0)

        val avg = lst.average()
        var sum = 0
        for (i in 0 until lst.size) {
            if (avg < lst[i]) sum++
        }
        println("%.3f%%".format(sum * 100 / lst.size.toDouble()))
    }
}