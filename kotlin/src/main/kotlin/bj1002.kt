import java.lang.Math.*

fun main() {
    val test = readln().toInt()

    for (i in 0 until test) {
        val e = readln().split(" ").map { it.toDouble() }
        var (x1, y1, r1,x2,y2) = e
        var r2 = e[5]
        var d1 = sqrt(pow(x1 - x2, 2.0) + pow(y1 - y2, 2.0))
        var d2 = r1 + r2;
        if (x1 == x2 && y1 == y2 && r1 == r2)
        {
            println("-1")
        }
        else
        {
            if (d1 > d2 || (x1 == x2 && y1 == y2) || abs(r1 - r2) > d1)
            {
                println("0")
            }
            else if (d1 == d2 || abs(r1 - r2) == d1)
            {
                println("1")
            }
            else
            {
                println("2")
            }
        }
    }
}