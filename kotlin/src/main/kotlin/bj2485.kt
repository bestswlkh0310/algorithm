fun main() {
    val n = readln().toInt()

    var arr = ArrayDeque<Int>()
    for (i in 0 until n) {
        val a = readln().toInt()
        arr.add(a)
        if (i == 0) continue
        arr[i - 1] = arr[i] - arr[i - 1]
    }
    arr.removeLast()
    var arrLen = arrayListOf<Int>()
    arrLen.addAll(arr)


    // 모든 간격들의 최대 공약수 구하기
    for (i in 0 until n - 2) {
        arr[i + 1] = gcd(arr[i], arr[i + 1])
    }
//    println(arrLen)

    val interval = arr.last()
    var sum = 0
    for (i in 0 until n - 1) {
        sum += arrLen[i] / interval - 1
    }
    println(sum)
}

private fun gcd(a: Int, b: Int): Int = if (b != 0) gcd(b, a % b) else a