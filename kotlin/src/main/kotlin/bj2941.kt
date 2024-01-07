fun main() {
    var str = readln().toCharArray()
    var sum = 0
    for (i in 0 until str.size - 2) {
        val chr = str.slice(i..i+2).joinToString("")
        if (chr == "dz=") {
            str[i] = '1'
            str[i + 1] = '1'
            str[i + 2] = '1'
            sum++
        }
    }
    for (i in 0 until str.size - 1) {
        val chr = str.slice(i..i + 1).joinToString("")
        if (chr == "c=" || chr == "c-" || chr == "d-" || chr == "lj" || chr == "nj" || chr == "s=" || chr == "z=") {
            str[i] = '1'
            str[i + 1] = '1'
            sum++
        }
    }

    var str2 = str.joinToString("").replace("1", "")

    println(sum + str2.length)
}