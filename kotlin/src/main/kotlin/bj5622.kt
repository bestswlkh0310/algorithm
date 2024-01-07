fun main() {
    val arr = readln().toCharArray()

    var sum = 0
    for (i in arr) {
        val code = i.code - 64
        if (code in 1..3) sum += 3
        else if (code in 4..6) sum += 4
        else if (code in 7..9) sum += 5
        else if (code in 10..12) sum += 6
        else if (code in 13..15) sum += 7
        else if (code in 16..19) sum += 8
        else if (code in 20..22) sum += 9
        else if (code in 23..26) sum += 10
    }
    println(sum)
}

// 65 ~ 90