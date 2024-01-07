fun main() {
    val n = readln().toInt()
    for (i in 0 until n) {
        var str = readln()
        while (str.contains("()")) {
            str = str.replace("()", "")
        }
        if (str.contains("(") || str.contains(")")) println("NO")
        else println("YES")
    }
}