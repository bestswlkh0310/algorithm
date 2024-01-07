fun main() {
    val str = readln()
    var arr = arrayListOf<Char>()
    var s = arrayListOf<Char>()
    var isK = false
    for (i in str) {
        if (i == '<') {
            isK = true
            s.joinToString("").split(" ").forEach { it.toCharArray().reversed().joinToString("").forEach { arr.add(it) }; arr.add(' ') }
            s = arrayListOf()
        }
        if (isK) arr.add(i)
        else s.add(i)
        if (i == '>') isK = false
    }
//    println(s)
    s.joinToString("").split(" ").forEach { it.toCharArray().reversed().joinToString("").forEach { arr.add(it) }; arr.add(' ') }
    println(arr.joinToString(""))
}