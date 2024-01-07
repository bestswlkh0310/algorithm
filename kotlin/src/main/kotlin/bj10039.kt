fun main() {
    val arr = arrayListOf<Int>()
    repeat(5) {
        val n = readln().toInt()
        if (n < 40) {
            arr.add(40)
        } else {
            arr.add(n)
        }
    }
    println(arr.average().toInt())
}