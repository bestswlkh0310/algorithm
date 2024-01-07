fun main() {
    val n = readln().toInt()
    val arr = arrayListOf(0, 0)
    for (i in 0 until n) {
        arr[readln().toInt()]++
    }
    if (arr[0] > arr[1]) {
        println("Junhee is not cute!")
    } else {
        println("Junhee is cute!")
    }
}