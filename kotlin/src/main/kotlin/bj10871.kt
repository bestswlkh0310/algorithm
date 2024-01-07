fun main() {
    var list: MutableList<Int> = arrayListOf()
    for (i in 1..9) {
        list.add(readln().toInt())
    }
    println(list.max())
    println(list.indexOf(list.max()) + 1)
}
