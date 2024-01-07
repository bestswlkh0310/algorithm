fun main() {
    val n = readln().toInt()
    var arr = arrayListOf<String>()
    var str = arrayListOf<Char>()

    for (i in 0 until n) {
        arr.add(readln())
    }
    for (i in 0 until arr[0].length) {
        val c = arr[0][i] // 비교대상
        var same = true

        for (j in 0 until n) {
            if (c != arr[j][i]) {
                same = false
            }
        }
        if (same) str.add(c)
        else str.add('?')

        same = true
    }

    println(str.joinToString(""))
}