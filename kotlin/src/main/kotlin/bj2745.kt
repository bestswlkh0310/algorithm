fun main() {
    val arr = arrayListOf('0','1','2','3','4','5','6','7','8','9',
                                                    'A','B','C','D','E','F','G','H','I',
                                                    'J','K','L','M','N','O','P','Q','R',
                                                    'S','T','U','V','W','X','Y','Z')
    val (a, b) = readln().split(" ")
    var str = a.toCharArray()
    str.reverse()
    val n = b.toLong()
    var nW = 1L
    var sum = 0L

    for ((k, i) in str.withIndex()) {
        repeat(k - 1) {
            nW *= n
        }
//        println("--$k")
//        println(nW)
        sum += arr.indexOf(i) * nW
        nW = n
    }
    println(sum)
}