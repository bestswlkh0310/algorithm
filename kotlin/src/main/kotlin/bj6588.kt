import java.lang.StringBuilder
import kotlin.math.sqrt

fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()
    val sb = StringBuilder()
    val sosu = arrayListOf(2)
    ll@
    for (i in 3 .. 1000 step 2) {
        for (j in sosu) {
            if (i < j * 2) break
            if (i % j == 0) continue@ll
        }
        sosu.add(i)
    }
    while (true) {
        val n = br.readLine().toInt()
        if (n == 0) break
        var t = true
        for (j in sosu) {
            if ((n - 2) % j == 0 && (n - 2) != j) {
                t = false
                break
            }
        }
        if (t) {
            sb.append("$n = 2 + ${n - 2}\n")
            continue
        }

        loop@
        for (i in 1 .. 1000000 step 2) {
//            println(i)
            if (i == 1 || n - i == 1) continue@loop
            for (j in sosu) {
                if ((n - j) > n) continue@loop
                if ((i % j == 0 && i != j) || ((n - i) % j == 0 && (n - i) != j)) {
                    if (i >= n) {
                        sb.append("Goldbach's conjecture is wrong.\n")
                        break@loop
                    }
//                    println("$i $j")
                    continue@loop
                }
            }
            sb.append("$n = $i + ${n - i}\n")
            break@loop
        }
    }
    bw.write("$sb")
    bw.flush()
    bw.close()
}