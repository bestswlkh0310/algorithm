import java.math.BigInteger

private var arr: MutableList<BigInteger> = Array (1000004) { BigInteger("0") }.toMutableList()
fun main() {

    arr[0] = BigInteger.ZERO
    arr[1] = BigInteger.ONE
    arr[2] = BigInteger.ONE

    val n = readln().toInt()
    var i = 0
    while (i != n) {
        arr[i + 2] = (arr[i + 1] + arr[i]) % BigInteger("1000000007")
        i++
    }
    println(arr[n])
}