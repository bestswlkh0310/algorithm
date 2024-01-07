fun main() {
    val lst = readln().split(" ").map { it.toInt() }
    var i = lst.min()
    while (lst.count { i % it == 0 } < 3) {
        i++
    }
    println(i)
}