fun main() {
    val a = readln().toInt()
    val b = readln().toInt()
    val c = readln().toInt()

    val sum = (a * b * c).toString().toCharArray()
    var arr = Array (10) { 0 }

    for (i in 0 until sum.size) {
//        println(sum[i])
        arr[sum[i].toString().toInt()]++
    }
    for (i in 0 .. 9) {
        println(arr[i])
    }
}