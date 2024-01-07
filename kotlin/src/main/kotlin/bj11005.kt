fun main() {
    val arr = arrayListOf('0','1','2','3','4','5','6','7','8','9',
        'A','B','C','D','E','F','G','H','I',
        'J','K','L','M','N','O','P','Q','R',
        'S','T','U','V','W','X','Y','Z')

    var str = arrayListOf<Char>()
    var (a, n) = readln().split(" ").map { it.toInt() }
    while (a != 0) {
        str.add(arr[a % n])
        a /= n
    }
    println(str.reversed().joinToString(""))
}