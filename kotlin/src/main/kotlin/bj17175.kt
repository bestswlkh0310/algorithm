private var arr = Array (55) { 0 }
fun main() {

    arr[0] = 1
    arr[1] = 1
    val inp = readln().toInt()

    for(i in 2 .. inp) {
        arr[i] = (1 + arr[i - 2] + arr[i - 1]) % 1000000007
    }
    println(arr[inp])
}

// 2^2 * 3^1 => 3 * 2