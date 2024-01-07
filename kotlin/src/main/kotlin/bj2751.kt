fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()
    val n = br.readLine().toInt()
    val arr = ArrayDeque<Int>()
    for (i in 0 until n) {
        arr.add(br.readLine().toInt())
    }
    arr.sort()
    for (i in 0 until n) {
        bw.write("${arr[i]}\n")
    }
    bw.flush()
    bw.close()
}