import kotlin.math.round

fun main() {
    val n = readln().toInt()
    var arr = ArrayDeque<Int>()
    var nArr = Array (8010) { 0 }

    for (i in 0 until n) {
        val a = readln().toInt()
        arr.add(a)
        nArr[a + 4004]++
    }
    arr.sort()
    println("%.0f".format(arr.average()))
    println(arr[arr.size / 2])
    val mxIdx = nArr.indexOf(nArr.max()) - 4004
    // 0 4 1 2 3 4
    // max == it => it의 인덱스 값
    var ar = arrayListOf<Int>()
    if (nArr.count { it == mxIdx } != 1) {
        var ar = arrayListOf<Int>()

        try {
            while (true) {
                println(1)
                nArr.forEach { if (nArr.max() == it) ar.add(it); nArr[nArr.indexOf(it)] = 0 }
            }
        } catch (e: Exception) {}
        println(ar.sorted()[1])
    }
    else println(mxIdx)
    println(arr.max() - arr.min())
}