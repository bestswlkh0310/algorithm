import kotlin.math.sqrt

fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()
    var sb = StringBuilder()

    val inp = br.readLine().toInt()
    var sosuArr = ArrayDeque<Int>()
    sosuArr.add(2)
    loop1@
    for (i in 3 until 1000 step 2) {
        for (j in sosuArr) {
            if (i % j == 0) continue@loop1
        }
        sosuArr.add(i)
    }
    // 테스트 케이스
    for (s in 0 until inp) {
        var n = br.readLine().toInt()

        var sum = 0
        // a + b = n (a, b는 소수)
        loop@
        for (a in 2 .. n / 2) {
            val b = n - a
/*            // 짝수면 패스
            if (a % 2 == 0 && a != 2) continue@loop
            if (b % 2 == 0 && b != 2) continue@loop
            // 합성수면 패스
            for (j in 3 .. sqrt(a.toDouble()).toInt() step 2)
                if (a % j == 0 && n != j) continue@loop
            for (j in 3 .. sqrt((n - a).toDouble()).toInt() step 2)
                if (b % j == 0 && b != j) continue@loop*/

            // 소수면 패스
            for (sosu in sosuArr) {
                if (a % sosu == 0 && a != sosu) continue@loop
                if (b % sosu == 0 && b != sosu) continue@loop
            }
            sum++
        }
        sb.append("$sum\n")
    }
    bw.write("$sb")
    bw.flush()
    bw.close()
}
