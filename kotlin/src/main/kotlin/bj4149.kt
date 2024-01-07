fun main() {
    var n = readln().toLong()
    //println(n)
    var nVal = n
    var sosu = arrayListOf<Long>(2,3,5,7,11,13,17,23,29,31,37)
    for (i in 0 until nVal / 2) {
        Hello@
        for (j in sosu) {
            if (n % j == 0L) {
                println(j)
                n /= j
                break
            }
            for (k in j + 1 until nVal step 2) {
                if (n % k == 0L) {
                    println(k)
                    n /= k
                    break@Hello
                }
            }
        }
    }
}