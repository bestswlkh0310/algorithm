fun main() {
    val arr: MutableList<Int> = readln().split(" ").map { it.toInt() }.toMutableList()

    var best = clockNum(arr)
    var sum = 0

    var clockArr: MutableList<Int> = arrayListOf()

    loop@
    for (i in 1 .. 9) {
        for (j in 1 .. 9) {
            for (k in 1 .. 9) {
                for (l in 1 .. 9) {
                    var num = clockNum(arrayListOf(i, j, k, l))
                    if (clockArr.contains(num)) {
                        continue
                    } else {
                        clockArr.add(num)
                        sum++
                        if (num == best) break@loop
                    }
                }
            }
        }
    }
    println(sum)
}

private fun clockNum(arr: MutableList<Int>): Int {
    var best = 10000

    for (i in 0 until 4) {
        val t = arr.joinToString("").toInt()
        if (t < best) best = t
        arr.add(0, arr[3])
        arr.removeAt(4)
    }
    return best
}