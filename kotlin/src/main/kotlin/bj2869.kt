import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.ceil

fun main() {
    val inp = BufferedReader(InputStreamReader(System.`in`)).readLine().split(" ").map { it.toInt() }
    var day = 1

    // 수열 => 시간 초과
/*    var sum = inp[0]
    while (sum < inp[2]) {
        day++
        sum += -inp[1] + inp[0]
        if (sum >= inp[2]) break
    }
    println(day)*/
    println("%d".format(ceil((inp[2] - inp[1]) / (inp[0] - inp[1]).toDouble()).toInt()))
}