fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()/*

    val n = br.readLine().toInt()
    val arr = ArrayDeque<Int>()
    for (i in 0 until n) {
        arr.add(br.readLine().toInt())
    }
    arr.sorted().forEach { bw.write("${it}\n") }
    bw.flush()
    bw.close()*/
    val arr = IntArray (10003) { 0 }
    val n = br.readLine().toInt()
    repeat (n) {
        arr[br.readLine().toInt()]++
    }
    for (i in 0 until 10003)
        for (j in 0 until arr[i])
            bw.write("$i\n")
    bw.flush()
    bw.close()
}