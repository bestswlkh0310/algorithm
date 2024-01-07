fun main() {
    val a = readln().toInt()
    val arr1 = readln().split(" ").map { it.toInt() }.toSet()
    val b = readln().toInt()
    val arr2 = readln().split(" ").map { it.toInt() }

    for (i in arr2) {
        if (arr1.contains(i)) println(1)
        else println(0)
    }
}