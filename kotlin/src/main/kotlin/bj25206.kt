fun main() {
    val arr = arrayListOf<String>("A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F")
    val arr1 = arrayListOf<Double>(4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0)

    var sum1 = 0.0
    var sum2 = 0.0
    for (i in 0 until 20) {
        val (a, b, c) = readln().split(" ")
        if (c == "P") continue
            sum1 += b.toDouble()
            sum2 += b.toDouble() * arr1[arr.indexOf(c)]
    }
    println(sum2 / sum1)
}