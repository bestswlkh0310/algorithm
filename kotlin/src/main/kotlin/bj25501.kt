private var sum = 0
fun main() {
    val n = readln().toInt()
    for (i in 0 until n) {
        val inp = readln()
        println("${re(inp, 0, inp.length - 1)} $sum")
        sum = 0
    }
}

fun re(str: String, left: Int, right: Int): Int {
    sum++
    if (left >= right) return 1
    else if(str[left] != str[right]) return 0
    else return re(str, left + 1, right - 1)
}