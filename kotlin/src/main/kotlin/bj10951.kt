fun main() {
    try {
        while (true){
            val (a, b) = readln().split(" ").map { it.toInt() }
            println(a + b)
        }
    } catch (e: Exception) {}
}