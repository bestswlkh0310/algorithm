fun main() {
    val n = readln().toInt()
    repeat(n) {
        val str = readln()
        val arr = str.split(" ").toMutableList()
        for ((i, j) in arr.withIndex()) {
            arr[i] = j.reversed()
        }
        for (i in arr) {
            print("$i ")
        }
    }
}