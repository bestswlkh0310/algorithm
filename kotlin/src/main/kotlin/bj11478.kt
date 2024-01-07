fun main() {
    var set = hashSetOf<String>()
    val str = readln()

    for (i in 0 until str.length) {
        for (j in 0 until str.length - i) {
            set.add(str.slice(j .. j + i))
        }
    }
    println(set.size)
}