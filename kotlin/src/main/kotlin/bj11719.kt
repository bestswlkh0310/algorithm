fun main() {
    val arr = arrayListOf<String>()
    try {
        while (true) {
            arr.add(readln())
        }
    } catch (_: Exception) {}
    for (i in arr) {
        println(i)
    }
}