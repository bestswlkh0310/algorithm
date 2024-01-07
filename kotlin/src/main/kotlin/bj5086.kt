fun main() {
    while (true) {
        var (a, b) = readln().split(" ").map { it.toInt() }
        if (a == 0 && b == 0) return
        if (a % b == 0) {
            println("multiple")
        } else if (b % a == 0) {
            println("factor")
        } else {
            println("neither")
        }
    }
}