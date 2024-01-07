fun main() {
    val a = readln()
    if (a == "  " || a == " " || a == "") return println(0)
    val inp = a.toCharArray().toMutableList()
    if (inp[0] == ' ') inp.removeAt(0)
    if (inp.last() == ' ') inp.removeLast()
    println(inp.joinToString("").split(" ").size)
}