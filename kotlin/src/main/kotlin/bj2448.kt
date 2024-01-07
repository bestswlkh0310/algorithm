val w = System.`in`.bufferedReader().readLine().toInt()
val b = Array(w) { Array(w * 2) { false } }
fun main() {
    val bw = System.out.bufferedWriter()
    val sb = StringBuilder()
    if (w == 3) {
        println("""  *  
 * * 
*****""")
        return
    }

    for (i in 0 until w) {
        for (j in 0 until w * 2) {
            if (j >= w - i && j <= w + i)
                b[i][j] = true
        }
    }
    roll(w / 2, w / 2, w, true)

    for (i in 0 until w) {
        for (j in 1 until w * 2)
            sb.append(if (b[i][j]) '*' else ' ')
        sb.append("\n")
    }
    bw.write("$sb")
    bw.flush()
    bw.close()
}

private fun roll(x1: Int, y1: Int, len: Int, mode: Boolean) {
    if (len == 1) return
    for (i in 0 until len / 2) {
        for (j in 1 until len) {
            if (len == 3 && j == 2 && i == 0) {
                b[y1][x1 + 1] = mode
                b[y1 - 1][x1 + 2] = false
                continue
            }
            if (j > i && j < len - i)
                b[i + y1][j + x1] = false
        }
    }
    roll(x1 + len / 4, y1 - len / 4, len / 2, true)
    roll(x1 - len / 4, y1 + len / 4, len / 2, false)
    roll(x1 + len - len / 4, y1 + len / 4, len / 2, false)
}