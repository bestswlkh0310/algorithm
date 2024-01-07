fun main() {
    val str = readln().toCharArray()
    val arr = arrayListOf<String>()
    for (i in str) {
        val arr1 = arrayListOf<String>()
        var n = i.toString().toInt()
        repeat(3) {
            arr1.add((n % 2).toString())
            n /= 2
        }
        arr.add(arr1.joinToString("").reversed())
    }
    var s = arr.joinToString("")
    while (s.first() == '0') {
        s = s.slice(1 until s.length)
    }
    println(s)
}