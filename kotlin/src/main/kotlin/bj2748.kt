fun main() {

    arr[0] = 0
    arr[1] = 1
    arr[2] = 1

    val inp = readln().toInt()
    println("${fibonacci(inp)}")
}
private var arr: MutableList<Long> = Array (91) { 0L }.toMutableList()

private fun fibonacci(n: Int): Long {
    if (n == 0) {
        return 0
    } else if (n == 1) {
        return 1
    } else {
        if (arr[n] != 0L) return arr[(n-1)] + arr[(n-2)]
        arr[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return arr[n]
    }
}