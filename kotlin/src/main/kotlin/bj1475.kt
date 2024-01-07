fun main() {
    val str = readln().toMutableList()
    for ((i, j) in str.withIndex()) {
        if (j == '6') {
            str[i] = '9'
        }
    }
    var sum = 0
    while (str.isNotEmpty()) {
        sum++
        for (i in 0 .. 9) {
            var c = (i + '0'.code).toChar()
            if (c == '6') c = '9'
            try {
                str.remove(c)
            } catch (e: Exception) {}
        }
    }
    println(sum)
}