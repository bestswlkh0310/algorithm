fun main() {
    readln().split(" ").map { it.toInt() }.sorted().forEach { print("$it ") }
}