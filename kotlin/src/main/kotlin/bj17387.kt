import java.lang.Exception
import java.lang.Long.min

fun main() {
//    for (i in 0 until 9) {

    val (x1, y1, x2, y2) = readln().split(" ").map { it.toLong() }
    val (x3, y3, x4, y4) = readln().split(" ").map { it.toLong() }

//    if (a1 == a2 && b1 != b2) return println(0)
    if ((x1 == x3 && y1 == y3) || (x2 == x4 && y2 == y4) || (x2 == x3 && y2 == y3) || (x1 == x4 && y1 == y4)) return println(1)

    var x = 0L
    var y = 0L
    try {
        //println(-x3 * (y4 - y3) / (x4 - x3) + y3 - y1 + x1 * (y2 - y1) / (x2 - x1))
        x = (-x3 * ((y4 - y3) / (x4 - x3)) + y3 - y1 + x1 * ((y2 - y1) / (x2 - x1))) / ((y2 - y1) / (x2 - x1) - (y4 - y3) / (x4 - x3))
    } catch (e: Exception) {
        //x 값이 정해지지 않으면
        try {
            // 기울기가 같으면
            val minFY = min(y1, y2)
            val minGY = min(y3, y4)
            val minFX = min(x1, x2)
            val minGX = min(x3, x4)
            if (x1 == x2 && x3 == x4 && ((y1 in minGY .. y3 + y4 - minGY) || (y2 in minGY .. y3 + y4 - minGY) || (y3 in minFY .. y1 + y2 - minFY) || (y4 in minFY .. y1 + y2 - minFY))) {
                return println(1)
            }
            if (y1 == y2 && y3 == y4 && ((x1 in minGX .. x3 + x4 - minGX) || (x2 in minGX .. x3 + x4 - minGX) || (x3 in minFX .. x1 + x2 - minFX) || (x4 in minFX .. x1 + x2 - minFX))) {
                return println(1)
            }
            if ((y1 - y2) / (x1 - x2) == (y3 - y4) / (x3 - x4)) {
                lastCheck(x1, y1, x2, y2, x3, y3, x4, y4, x1, y1)
                return
            }
        } catch (e: Exception) {}

        if (x1 == x2 && y3 == y4) {
            val minY = min(y1, y2)
            val minX = min(x3, x4)
            if (y3 in minY .. y2 + y1 - minY && x1 in minX .. x4 + x3 - minX) return println(1)
            else return println(0)
        }
        if (x3 == x4 && y1 == y2) {
            val minY = min(y3, y4)
            val minX = min(x1, x2)
            if (y1 in minY .. y4 + y3 - minY && x3 in minX .. x2 + x1 - minX) return println(1)
            else return println(0)
        }

        if (x1 == x2) {
            val minX = min(x3, x4)
            y = f(x3, y3, x4, y4, x1)
            val minY = min(y1, y2)
            if (x1 in minX .. x3 + x4 - minX && y in minY .. y4 + y3 - minY) return println(1)
            else return println(0)
        } else if (x3 == x4) {
            val minX = min(x1, x2)
            y = f(x1, y1, x2, y2, x3)
            val minY = min(y3, y4)
            if (x1 in minX .. x1 + x2 - minX && y in minY .. y2 + y1 - minY) return println(1)
            else return println(0)
        } else if (y1 == y2) {
            val minY = min(y3, y4)
            val minX = min(x3, x4)
            x = f(y1, x1, y2, x2, y1)
            if (x in minX .. x3 + x4 - minX && y1 in minY .. y4 + y3 - minY) return println(1)
            else return println(0)
        } else if (y3 == y4) {
            val minY = min(y1, y2)
            val minX = min(x1, x2)
            x = f(y3, x3, y4, x4, y3)
            if (x in minX .. x1 + x2 - minX && y3 in minY .. y2 + y1 - minY) return println(1)
            else return println(0)
        }
        return
        /*        val y = f(x1, y1, x2, y2, x)
                lastCheck(x1, y1, x2, y2, x3, y3, x4, y4, x, y)
                return*/
    }
    y = f(x1, y1, x2, y2, x)
    lastCheck(x1, y1, x2, y2, x3, y3, x4, y4, x, y)
//    println("$x $y")
//    }

}
fun lastCheck(x1: Long, y1: Long, x2: Long, y2: Long, x3: Long, y3: Long, x4: Long, y4: Long, x: Long, y: Long) {
    val minFX = min(x1, x2)
    val maxFX = x1 + x2 - minFX

    val minGX = min(x3, x4)
    val maxGX = x3 + x4 - minGX

    val minFY = min(y1, y2)
    val maxFY = y1 + y2 - minFY

    val minGY = min(y3, y4)
    val maxGY = y3 + y4 - minGY

    if (x in minFX..maxFX && x in minGX .. maxGX && y in minFY .. maxFY && y in minGY .. maxGY) println(1)
    else println(0)
}

fun f(x1: Long, y1: Long, x2: Long, y2: Long, x: Long): Long {
    return (y2 - y1) / (x2 - x1) * (x - x1) + y1
}


//2 -2 2 -5
//2 -3 2 -4