fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()
    var sb = StringBuilder()
    val n = br.readLine().toInt()
    val init = System.currentTimeMillis()
/*    var aa = ArrayDeque<Char>()
    aa.addAll(List(n) { '*' })
    val arr: ArrayDeque<ArrayDeque<Char>> = ArrayDeque()
    arr.addAll(List(n) { aa })*/

    var arr = Array(n) { ArrayDeque(List(n) { '*' }) }
    roll(arr, 0, 0, n)
    for (i in 0 until n) {
        for (j in 0 until n) {
            sb.append(arr[i][j])
        }
        sb.append("\n")
    }
    bw.write("$sb\n")
//    bw.write("${System.currentTimeMillis() - init} ms")
    bw.flush()
    bw.close()
}

private fun roll (arr: Array<ArrayDeque<Char>>, x: Int, y: Int, width: Int) {
    if (width == 1 / 3) return
    for (i in width / 3 until width / 3 * 2) {
        for (j in width / 3 until width / 3 * 2) {
            arr[i + x][j + y] = ' '
        }
    }
    for (i in 0 until 3) {
        for (j in 0 until 3) {
            if (j == 1 && i == 1) continue
            roll(arr, i * width / 3 + x, j * width / 3 + y, width / 3)
        }
    }
}