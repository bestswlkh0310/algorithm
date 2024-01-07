import java.lang.StringBuilder

fun main() {
    val n = readln().toInt()
    val sb = StringBuilder()
    val 스택 = ArrayDeque<Int>()
    for (i in 1 .. n) {
        스택.add(i)
    }
    val 스택1 = ArrayDeque<Int>()
    for (i in 0 until n) {
        val inp = readln().toInt()
        println(inp)
        try {
            while (스택.first() <= inp) {
                println(1)
                스택1.add(스택.first())
                스택.removeFirst()
                sb.append("+\n")
            }
        } catch (e: Exception) { }

        println()
        println(스택)
        println(스택1)
        if (스택1.last() == inp) {
            스택.add(스택1.last())
            스택1.removeLast()
            sb.append("-\n")
        }
        else if (스택1.size == 0) {
            return println("NO")
        }
    }
    println(sb)
}