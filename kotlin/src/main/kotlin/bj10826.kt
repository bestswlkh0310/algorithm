import java.math.BigInteger

private var arr: MutableList<BigInteger> = Array (10001) { BigInteger("0") }.toMutableList()
fun main() {

    arr[0] = BigInteger.ZERO
    arr[1] = BigInteger.ONE
    arr[2] = BigInteger.ONE

    val inp = readln().toInt()
    println("${fibonacci(inp)}")
}
private fun fibonacci(n: Int): BigInteger {
    if (n == 0) {
        return BigInteger.ZERO
    } else if (n == 1) {
        return BigInteger.ONE
    } else {
        if (arr[n] != BigInteger.ZERO) return arr[(n-1)] + arr[(n-2)]
        arr[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return arr[n]
    }
}