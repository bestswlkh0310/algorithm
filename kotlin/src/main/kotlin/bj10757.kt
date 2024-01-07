import java.lang.Integer.*

fun main() {
    val (a, b) = readln().split(" ")

    var arrA: MutableList<String> = arrayListOf()
    var arrB: MutableList<String> = arrayListOf()

    var sliceSize = 9

    for (i in 0 until a.length / sliceSize)
        arrA.add(a.slice(sliceSize * i + a.length % sliceSize until sliceSize * i + a.length % sliceSize + sliceSize))
    if (a.length % sliceSize != 0) arrA.add(0, a.slice(0 until a.length % sliceSize))

    for (i in 0 until b.length / sliceSize)
        arrB.add(b.slice(sliceSize * i + b.length % sliceSize until sliceSize * i + b.length % sliceSize + sliceSize))
    if (b.length % sliceSize != 0) arrB.add(0, b.slice(0 until b.length % sliceSize))

    val minSize = min(arrA.size, arrB.size)
    val maxSize = max(arrA.size, arrB.size)
    var arrSum: MutableList<Int> = arrayListOf()

    var arrSumA = arrA.map { it.toInt() }.toMutableList()
    var arrSumB = arrB.map { it.toInt() }.toMutableList()

    arrSumA.reverse()
    arrSumB.reverse()

//    println(arrSumA)
//    println(arrSumB)

    for (i in 0 until minSize) {
        arrSum.add(arrSumA[i] + arrSumB[i])
    }

    for (i in minSize until maxSize) {
        if (arrSumA.size == maxSize) {
            arrSum.add(arrSumA[i])
        }
        if (arrSumB.size == maxSize) {
            arrSum.add(arrSumB[i])
        }
    }

    println(arrSum)

    if (a.length == 1 && b.length == 1) return println(a.toInt() + b.toInt())
    for (i in 0 until arrSum.size - 1) {
        val num = arrSum[i]
        if (num.toString().length % sliceSize == 1) {
            arrSum[i + 1] += arrSum[i].toString()[sliceSize - 1].toString().toInt()
            arrSum[i] = arrSum[i].toString().slice(1 .. sliceSize).toInt()
        }
    }

    arrSum.reverse()
    arrSum.forEach { print(it) }

/*    println(arrSumA)
    println(arrSumB)
    println(arrSum)*/
}