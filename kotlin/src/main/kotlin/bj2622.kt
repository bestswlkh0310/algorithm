import kotlin.math.*
fun main() {
    // a + b + c = n (n은 상수 / a, b, c는 자연수)
    // 경우의 수를 구해라 ((1,2,3), (2,1,3)은 같은 경우)
    // 삼각형 조건 맞추기
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()
    var n = br.readLine().toInt()
    var sum = 0

    for (i in 1 until n) {
        for (j in i until n) {
            val k = n - i - j
            if (j > k) break
            if (i + j > k) sum++
        }
    }
    println(sum)
    bw.flush()
    bw.close()
}