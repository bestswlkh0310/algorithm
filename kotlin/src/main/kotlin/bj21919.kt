fun main() {
    val n = readln().toInt()
    var arr = readln().split(" ").map { it.toLong() }.toSet().toMutableList()
    val sosu = arrayListOf(2L, 3L, 5L)
    loop@
    for (i in 3 .. arr.max() step 2) {
        for (j in sosu) {
            if (i % j == 0L) continue@loop
        }
        sosu.add(i)
    }
    println(123)
    arr = arr.filter { it in sosu }.toMutableList()
    if (arr.isEmpty()) {
        println(-1)
    } else {
        for (i in 0 until arr.size - 1) {
            arr[i + 1] = arr[i] * arr[i + 1] / gcd(arr[i], arr[i + 1])
        }
        println(arr.last())
    }
}

private fun gcd(a: Long, b: Long): Long {
    if (b != 0L) {
        return gcd(b, a % b)
    } else {
        return a
    }
}