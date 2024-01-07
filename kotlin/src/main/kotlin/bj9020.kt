fun main() {
    val inp = readln().toInt()
    for (j in 0 until inp) {
        var m = readln().toInt()
        var arr: MutableList<Int> = arrayListOf()
        if (m == 2) {

        }
        for (i in 2 .. m / 2) {
            var n = m
            if (isPrime(i)) {
                n -= i
                if (isPrime(n)) {
                    arr.add(i)
                }
            }
        }
        println("${arr[arr.size - 1]} ${m - arr[arr.size - 1]}")
    }
}

fun isPrime(n: Int): Boolean {
    if (n <= 1) return false
    if (n == 2) return true
    if (n % 2 == 0) return false
    for (i in 3 .. n / 2 step 2) {
        if (n % i == 0) return false
    }
    return true
}