fun main() {
    try {
        while (true) {
            var inp1 = readln()
            var inp = inp1.split(".")
            var so = inp[1].split("(")[1]
            so = so.substring(0, so.length - 1)
//    println(so)
            val cnt0 = inp[1].split("(")[0].length
            var f = inp[0] + inp[1].split("(")[0]
//    println(f)
            val cnt9 = so.length
            val all = f + so
            var b = ""
            for (i in 0 until cnt9) {
                b = b.plus("9")
            }
            for (i in 0 until cnt0) {
                b = b.plus("0")
            }
            val a = all.toInt() - f.toInt()
//    println(a)

            val ss = gcd(a, b.toInt())
//    println(b)
//    println(ss)

            println("$inp1 = ${a / ss} / ${b.toInt() / ss}")
        }
    } catch (e: Exception) {}

}
private fun gcd(a: Int, b:Int): Int = if(b != 0) gcd(b, a % b) else a