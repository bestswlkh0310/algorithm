private var sum0 = 0
private var sum1 = 0

fun main() {
    val n = readln().toInt()

    arr[0] = 0
    arr[1] = 1
    arr[2] = 1

    for (i in 0 until n){
        val inp = readln().toInt()
        if (inp == 0) {
            println("1 0")
            continue
        }
        if (inp == 1) {
            println("0 1")
            continue
        }
        println("${fibonacci(inp - 1)} ${fibonacci(inp)}")
    }
}
private var arr: MutableList<Int> = Array (41) { 0 }.toMutableList()

private fun fibonacci(n: Int): Int {
    if (n == 0) {
        return 0
    } else if (n == 1) {
        return 1
    } else {
        if (arr[n] != 0) return arr[n-1] + arr[n-2]
        arr[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return arr[n]
    }
}