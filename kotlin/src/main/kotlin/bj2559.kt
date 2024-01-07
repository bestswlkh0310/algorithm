fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()

    val (n, a) = br.readLine().split(" ").map { it.toInt() }
    val arr = br.readLine().split(" ").map { it.toInt() }

    var sum = -101

    for (i in 0 .. n - a) {
        var tmpSum = arr.slice(i until a + i).sum()
        if (tmpSum > sum) sum = tmpSum
    }
    bw.write("$sum")
    bw.flush()
    bw.close()
}