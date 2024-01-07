import kotlin.math.abs
// failfail
fun main() {
    val br = System.`in`.bufferedReader()
    val (n, c) = br.readLine().split(" ").map { it.toInt() }

    var arr: MutableList<MutableList<Int>> = Array (2) { Array (n) { 99999999 }.toMutableList() }.toMutableList()

    for (i in 0 until n) {
        arr[0][i] = (br.readLine().toInt())
        if (i == 0) continue
        arr[1][i-1] = abs(arr[0][i] - arr[0][i - 1])
    }
    br.close()

/*    // 시간 초과 후보
    for (i in 0 until n - 1) {
        arr[1].add(arr[0][i + 1] - arr[0][i])
    }*/
    var min = arr[1].min()

    if (n == c) return println(min)

    var minIdx: Int
    var minCount = arr[1].count{ it == min }

    while (arr[1].size >= c) {
        //println(arr[1])
        if (minCount == 0) {
            val reMin = arr[1].min()
            min = reMin
            minCount = arr[1].count { it == min }
        }
        minCount--
        minIdx = arr[1].indexOf(min)
        println("minCount : $minCount, min : $min, minIdx: $minIdx")
        if (minIdx >= 0 && minIdx < arr[1].size - 1) {
            val arrM = arr[1][minIdx]
            if (minIdx > 0 && arr[1][minIdx - 1] < arr[1][minIdx + 1]) {
                arr[1][minIdx - 1] += arrM
                arr[1].removeAt(minIdx)
            } else if (minIdx < arr[1].size - 2){
                arr[1][minIdx + 1] += + arrM
                arr[1].removeAt(minIdx)
            }
        }
/*        try {
            arr[1][minIdx - 1] = arr[1][minIdx - 1] + arr[1][minIdx]
            arr[1].removeAt(minIdx)
        } catch (e: Exception) {
            try {
                arr[1][minIdx + 1] = arr[1][minIdx + 1] + arr[1][minIdx]
                arr[1].removeAt(minIdx)
            } catch (e: Exception) {}
        }*/
/*        if (arr[1][minIdx - 1] is Int) {
            if (arr[1][minIdx - 1] > arr[1][minIdx + 1]) {
                arr[1][minIdx + 1] = arr[1][minIdx + 1] + arr[1][minIdx]
            } else {
                arr[1][minIdx - 1] = arr[1][minIdx - 1] + arr[1][minIdx]
            }
            arr[1].removeAt(minIdx)
        }*/
        //println(arr[1])
    }
    println(arr[1].min())
}

/*
5 3
1
2
8
4
9

=> 3

9 3
1
2
3
4
5
6
7
8
100

=> 7*/
