fun main() {
    val str = readln()
    val str1 = str.split("-")[0]
    val str2 = str.slice(str1.length + 1 until str.length)
    println(str1.split("+").sumOf { it.toInt() } - str2.split("-", "+").filter { it != "" }.sumOf { it.toInt() })
}
