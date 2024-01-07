fun main() {
    val str = readln().toCharArray()
    var isJava = false
    for (i in str) {
        if (i.code in 65..90) isJava = true
    }
    var arr = arrayListOf<Char>()
    if (isJava && str.contains('_') || str.last() == '_' || str.first() == '_' || str.joinToString("").contains("__") || str.first().code in 65..90)  {
        println("Error!")
    } else {
        if (isJava) {
            for ((j, i) in str.withIndex()) {
                if (i.code in 65 .. 90) {
                    if (j > 0) arr.add('_')
                    arr.add((i.code + 32).toChar())
                } else {
                    arr.add(i)
                }
            }
        } else {
            for ((i, j) in str.withIndex()) {
                if (j == '_') {
                    str[i + 1] = (str[i + 1].code - 32).toChar()
                }
            }
            str.filter { it != '_' }.forEach { arr.add(it) }
        }
    }
    println(arr.joinToString(""))
}