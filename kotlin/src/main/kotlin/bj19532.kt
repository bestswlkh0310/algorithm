fun main() {
    val arr = readln().split(" ").map { it.toDouble() }
    val a = arr[0]
    val b = arr[1]
    val c = arr[2]
    val d = arr[3]
    val e = arr[4]
    val f = arr[5]/*
    val x = (f - e * c / b) / (d - e * a / b)
    println("${x.toInt()} ${((c-a * x) / b).toInt()}")*/

    for (x in -999 .. 999) {
        for (y in -999 .. 999) {
            if (a * x + b * y == c && d * x + e * y == f) return println("$x $y")
        }
    }
}