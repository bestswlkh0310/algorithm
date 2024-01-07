fun main() {
    val str = readln().toCharArray()
    for ((i, j) in str.withIndex()) {
        if (j.isLowerCase()) str[i] = j.uppercaseChar()
        else str[i] = j.lowercaseChar()
    }
    println(str)
}