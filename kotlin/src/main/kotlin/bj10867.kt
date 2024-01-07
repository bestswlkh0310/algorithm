fun main() {
    val n = readln().toInt()
    val arr = readln().split(" ").map { it.toInt() }.toSet().toList().sorted()
    for (i in arr) {
        print("$i ")
    }
}