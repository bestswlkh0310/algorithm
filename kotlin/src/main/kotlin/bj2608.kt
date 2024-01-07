fun main() {
    val a = readln()
    val b = readln()

    R(a)
    R(b)
    println(sum)

    var str: MutableList<Char> = arrayListOf()
    while (sum != 0) {
        if (sum - 1000 >= 0) {
            sum -= 1000
            str.add('M')
            continue
        }
        if (sum - 900 >= 0) {
            sum -= 900
            str.add('C')
            str.add('M')
            continue
        }
        if (sum - 500 >= 0) {
            sum -= 500
            str.add('D')
            continue
        }
        if (sum - 400 >= 0) {
            sum -= 400
            str.add('C')
            str.add('D')
            continue
        }
        if (sum - 100 >= 0) {
            sum -= 100
            str.add('C')
            continue
        }
        if (sum - 90 >= 0) {
            sum -= 90
            str.add('X')
            str.add('C')
            continue
        }
        if (sum - 50 >= 0) {
            sum -= 50
            str.add('L')
            continue
        }
        if (sum - 40 >= 0) {
            sum -= 40
            str.add('X')
            str.add('L')
            continue
        }
        if (sum - 10 >= 0) {
            sum -= 10
            str.add('X')
            continue
        }
        if (sum - 9 >= 0) {
            sum -= 9
            str.add('I')
            str.add('X')
            continue
        }
        if (sum - 5 >= 0) {
            sum -= 5
            str.add('V')
            continue
        }
        if (sum - 4 >= 0) {
            sum -= 4
            str.add('I')
            str.add('V')
            continue
        }
        if (sum - 1 >= 0) {
            sum -= 1
            str.add('I')
            continue
        }
    }
    println(str.joinToString(""))
}
private var sum = 0

fun R(s: String) {
    var str = s
    if (str.contains("IV")) {
        str = str.replace("IV", "")
        sum += 4
    }
    if (str.contains("IX")) {
        str = str.replace("IX", "")
        sum += 9
    }
    if (str.contains("XL")) {
        str = str.replace("XL", "")
        sum += 40
    }
    if (str.contains("XC")) {
        str = str.replace("XC", "")
        sum += 90
    }
    if (str.contains("CD")) {
        str = str.replace("CD", "")
        sum += 400
    }
    if (str.contains("CM")) {
        str = str.replace("CM", "")
        sum += 900
    }
    for (i in str.toCharArray()) {
        when (i) {
            'I' -> sum += 1
            'V' -> sum += 5
            'X' -> sum += 10
            'L' -> sum += 50
            'C' -> sum += 100
            'D' -> sum += 500
            'M' -> sum += 1000
        }
    }
}