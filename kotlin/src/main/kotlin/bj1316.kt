import java.lang.Exception

fun main() {
    var result = 0

    var testCase = readln().toInt()

    loop@
    for (k in 1 .. testCase)
    {
        var str = readln().toCharArray()
        for (j in 0 until str.size - 1) {
            for (i in 0 until str.size - 1) {
                if (str[i] == str[i + 1]) str[i] = '1'
            }
        }
        var str2 = String(str).replace("1", "")
        for (chr1 in str2) {
            var sum = 0
            for (chr2 in str2) {
                if (chr1 == chr2) sum++
            }
            if (sum >= 2) continue@loop
        }
        result++
    }
    println(result)
}